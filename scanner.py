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
        session_num = 1
        
        while True:
            session_path = os.path.join(self.root_dir, "session" + str(session_num))
            if not os.path.exists(session_path):
                break
            
            session_num += 1

        os.mkdir(session_path)
        self.current_session_dir = session_path

    def scan(self):
        # TODO: validate that a session has started
        # TODO: take a series of pictures
        print("hi")

    def stop_session(self):
        # TODO: validate that session has started
        # TODO: stop the camera
        session_dir = self.current_session_dir
        self.current_session_dir = ""
        return Scan(session_dir, "9/26/23")

class Scan:
    directory_path = ""
    date = ""
    def __init__(self, directory_path, date):
        self.directory_path = directory_path
        self.date = date

    def to_dict(self):
        return dict(directory_path = self.directory_path, date = self.date)

class FileManager:
    database = TinyDB('database.json')

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


default_root_dir = "/home/crsz/Pictures/Scans/"
scanner = Scanner(default_root_dir)

file_manager = FileManager()

scanner.start_session()
print("New scanning session dir:\t" + scanner.current_session_dir + "\n")

scan = scanner.stop_session()
file_manager.insert_session(scan)
file_manager.show_database()