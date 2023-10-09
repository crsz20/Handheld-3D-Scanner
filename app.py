# Custom Dependencies
from Scanner import Scanner
from FileManager import FileManager

def main():
    default_root_dir = "/home/crsz/Pictures/Scans/"
    scanner = Scanner(default_root_dir)

    file_manager = FileManager()

    scanner.start_session()
    print("New scanning session dir:\t" + scanner.current_session_dir + "\n")

    scan = scanner.stop_session()
    file_manager.insert_session(scan)
    file_manager.show_database()



if __name__ == "__main__":
    main()