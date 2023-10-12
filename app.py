# External Dependancies
from curtsies import Input
# import cv2

# Custom Dependencies
from Scanner import Scanner
from FileManager import FileManager

PRIMARY_CONNECTION_STRING = "[primary connection string]"

def evaluate_buttons(file_manager, scanner):
    with Input(keynames='curses') as input_generator:

        # frame = scanner.camera.capture_array()
        # cv2.imshow("picam", frame)

        path = ""

        for button_press in input_generator:
            print(repr(button_press))
            if repr(button_press) == '\'s\'':
                print("scanning")
                if scanner.is_in_session == False:
                    print("New session")
                    path = file_manager.create_folder()
                    scanner.start_session(path)
                scanner.scan()
            
            if repr(button_press) == '\'q\'':
                print("Ending session")
                scan = scanner.stop_session()
                file_manager.insert_session(scan)
                file_manager.upload_to_azure_storage(PRIMARY_CONNECTION_STRING, path)

            if repr(button_press) == '\'e\'':
                return

def main():
    default_root_dir = "/home/crsz/Pictures/Scans/"
    file_manager = FileManager(default_root_dir)
    scanner = Scanner()

    evaluate_buttons(file_manager, scanner)

    file_manager.show_database()


## TODO: initialize accelerometer


if __name__ == "__main__":
    main()
