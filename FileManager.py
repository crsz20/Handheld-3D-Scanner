# External Dependencies
from tinydb import TinyDB, Query

class FileManager:
    database = TinyDB('database.json')

    def __init__(self):
        self.database.truncate()

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

