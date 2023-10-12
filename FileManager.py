# External Dependencies
import os, zipfile

from tinydb import TinyDB, Query

from azure.iot.device import IoTHubDeviceClient
from azure.core.exceptions import AzureError
from azure.storage.blob import BlobClient

class FileManager:
    database = TinyDB('database.json')
    root_dir = ""

    def __init__(self, root_dir):
        ## For clearing the database:
        self.database.truncate()
        self.root_dir = root_dir

    def create_folder(self):
        session_num = 1
        
        while True:
            session_path = os.path.join(self.root_dir, "session" + str(session_num))
            if not os.path.exists(session_path):
                break
            
            session_num += 1

        os.mkdir(session_path)
        return session_path

    def insert_session(self, scan):
        # Store filepath and date
        self.database.insert(scan.to_dict())

    def query_session(self):
        # TODO: Search for disired session
        print("hi")
    
    def show_database(self):
        print("===All scans in database===")
        for scan in self.database:
            print(scan)

    ############### Cloud ###############
    def upload_to_azure_storage(self, PRIMARY_CONNECTION_STRING, scan_file_path):
        # name = 'DirToZip'
        zip_name = scan_file_path + '.zip'

        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
            for folder_name, subfolders, filenames in os.walk(scan_file_path):
                for filename in filenames:
                    file_path = os.path.join(folder_name, filename)
                    zip_ref.write(file_path, arcname=os.path.relpath(file_path, scan_file_path))

        zip_ref.close()

        PATH_TO_FILE = r'{}'.format(zip_name) # Convert to raw string



        device_client = IoTHubDeviceClient.create_from_connection_string(PRIMARY_CONNECTION_STRING)

        try:
            print ("IoT Hub file upload sample, press Ctrl-C to exit")
            self.__run_sample(device_client, PATH_TO_FILE)
        except KeyboardInterrupt:
            print ("IoTHubDeviceClient sample stopped")
        finally:
            # Graceful exit
            device_client.shutdown()

    def __run_sample(self, device_client, PATH_TO_FILE):
        # Connect the client
        device_client.connect()

        # Get the storage info for the blob
        blob_name = os.path.basename(PATH_TO_FILE)
        storage_info = device_client.get_storage_info_for_blob(blob_name)

        # Upload to blob
        success, result = self.__store_blob(storage_info, PATH_TO_FILE)

        if success == True:
            print("Upload succeeded. Result is: \n") 
            print(result)
            print()

            device_client.notify_blob_upload_status(
                storage_info["correlationId"], True, 200, "OK: {}".format(PATH_TO_FILE)
            )

        else :
            # If the upload was not successful, the result is the exception object
            print("Upload failed. Exception is: \n") 
            print(result)
            print()

            device_client.notify_blob_upload_status(
            storage_info["correlationId"], False, result.status_code, str(result)
        )
    
    def __store_blob(self, blob_info, file_name):
        try:
            sas_url = "https://{}/{}/{}{}".format(
                blob_info["hostName"],
                blob_info["containerName"],
                blob_info["blobName"],
                blob_info["sasToken"]
            )

            print("\nUploading file: {} to Azure Storage as blob: {} in container {}\n".format(file_name, blob_info["blobName"], blob_info["containerName"]))

            # Upload the specified file
            with BlobClient.from_blob_url(sas_url) as blob_client:
                with open(file_name, "rb") as f:
                    result = blob_client.upload_blob(f, overwrite=True)
                    return (True, result)

        except FileNotFoundError as ex:
            # catch file not found and add an HTTP status code to return in notification to IoT Hub
            ex.status_code = 404
            return (False, ex)

        except AzureError as ex:
            # catch Azure errors that might result from the upload operation
            return (False, ex)

