from tinydb import TinyDB, Query

# A single Scan class will have a filepath
# for a single session of images and 3D generation.
# That is, a single directory_path & date will
# correspond to a set of images (input) and a
# single .obj file (output)
class Scan:
    directory_path = ""
    date = ""
    def __init__(self, directory_path, date):
        self.directory_path = directory_path
        self.date = date

    def to_dict(self):
        return dict(directory_path = self.directory_path, date = self.date)


db = TinyDB('db.json')
db.truncate()
scan1 = Scan("example/path1", "9/25/23")
scan2 = Scan("example/path2", "9/25/23")

db.insert(scan1.to_dict())
db.insert(scan2.to_dict())

scans = db.all()

for scan in scans:
    print(scan)

for item in db:
    print(item) 