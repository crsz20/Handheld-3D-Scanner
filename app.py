# External Dependancies
# from curtsies import Input
import sys
import select
from time import sleep
# import cv2

# Custom Dependencies
from Accelerometer import Accelerometer
from Scanner import Scanner
from FileManager import FileManager

PRIMARY_CONNECTION_STRING = "[primary connection string]"

def event_loop(accelerometer, file_manager, scanner):

    while(True):
        acceleration = accelerometer.compute_acceleration()
        angular_velocity = accelerometer.compute_angular_velocity()
        print("Gx=%.2f" %angular_velocity[0], u'\u00b0'+ "/s", "\tGy=%.2f" %angular_velocity[1], u'\u00b0'+ "/s", "\tGz=%.2f" %angular_velocity[2], u'\u00b0'+ "/s", "\tAx=%.2f g" %acceleration[0], "\tAy=%.2f g" %acceleration[1], "\tAz=%.2f g" %acceleration[2]) 
        path = ""

        input = select.select([sys.stdin], [], [], 1)[0]
        if input:
            value = sys.stdin.readline().rstrip()
            print(value)

            if (value == "s"):
                print("scanning")
                if scanner.is_in_session == False:
                    print("New session")
                    path = file_manager.create_folder()
                    scanner.start_session(path)
                scanner.scan()
            
            elif (value == "q"):
                print("Ending session")
                scan = scanner.stop_session()
                file_manager.insert_session(scan)
                file_manager.upload_to_azure_storage(PRIMARY_CONNECTION_STRING, path)

            elif (value == "d"):
                file_manager.show_database()


def main():
    accelerometer = Accelerometer()
    accelerometer.MPU_Init()
    sleep(1)

    default_root_dir = "/home/crsz/Pictures/Scans/"
    file_manager = FileManager(default_root_dir)
    scanner = Scanner()

    event_loop(accelerometer, file_manager, scanner)

    file_manager.show_database()


if __name__ == "__main__":
    main()
