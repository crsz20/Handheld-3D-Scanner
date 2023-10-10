# External Dependencies
import os
from tinydb import TinyDB, Query

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

