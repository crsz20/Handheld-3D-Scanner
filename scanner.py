import os # File directory management
from tinydb import TinyDB, Query

# Handles taking a photo and controlling system
# state. Then, hands the filepath + date to the database
def Scanner:
    root_dir = ""
    current_session_dir = ""
    # picam2 = Picamera2()
    ## TODO: initialize accelerometer

    def __init__(self, root_dir):
        self.root_dir = root_dir

    def start_session(self):
        # Make a new sub-directory
        print(os.path.exists(self.root_dir))


    def scan(self):
        # validate that a session has started

    def stop_session(self):
        # validate that session has started

def FileManager:
    database = TinyDB('database.json')

    def insert_session(self, dir):
        # store filepath and date

    def query_session(self):
        # Search for disired session


default_root_dir = "/home/crsz/Pictures/Scans/"
scanner = Scanner(default_root_dir)

file_manager = FileManager()