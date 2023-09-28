import os # File directory management
from tinydb import TinyDB, Query

# Handles taking a photo and controlling system
# state. Then, hands the filepath + date to the database
class Scanner:
    root_dir = ""
    current_session_dir = ""
    # picam2 = Picamera2()
    ## TODO: initialize accelerometer

    def __init__(self, root_dir):
        self.root_dir = root_dir

    def start_session(self):
        # Make a new sub-directory
        # print(os.path.exists(self.root_dir))
	session_num = 1
	
	while True:
		session_path = os.path.join(self.root_dir, str(session_num))
		if not os.path.exists(session_path):
			break
		
		session_num += 1

	os.mkdir(session_path)
	self.current_session_dir = session_path
	print(os.path.exists(self.current_session_dir))

    def scan(self):
        # validate that a session has started
        print("hi")

    def stop_session(self):
        # validate that session has started
        print("hi")

class FileManager:
    database = TinyDB('database.json')

    def insert_session(self, dir):
        # store filepath and date
        print("hi")

    def query_session(self):
        # Search for disired session
        print("hi")


default_root_dir = "/home/crsz/Pictures/Scans/"
scanner = Scanner(default_root_dir)

file_manager = FileManager()

scanner.start_session()
