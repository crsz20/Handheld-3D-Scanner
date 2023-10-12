# External Dependencies
from datetime import datetime
from dateutil import tz
from picamera2 import Picamera2

# Handles taking a photo and controlling system
# state. Then, hands the filepath + date to the database
class Scanner:
    camera = Picamera2()

    is_in_session = False
    current_session_dir = ""
    image_count = 0
        
    def __get_datetime(self):
        now = datetime.now()
        date = now.date()

        # Auto-detect timezone and convert from UTC format
        from_local_zone = tz.tzutc()
        to_local_zone = tz.tzlocal()
        utc = now.replace(tzinfo=from_local_zone)
        localized_timesamp = utc.astimezone(to_local_zone)

        date_str = str(date.month) + "/" + \
                   str(date.day) + "/" + \
                   str(date.year)
        timestamp_str = str(localized_timesamp.hour) + ":" + \
                        str(localized_timesamp.hour) + ":" + \
                        str(localized_timesamp.second)
        
        return (date_str, timestamp_str)


    def start_session(self, session_path):   
        if self.is_in_session == False:
            self.is_in_session = True
            print(self.is_in_session)   
            self.current_session_dir = session_path
            self.camera.start()
        else:
            print("There is already an ongoing scanning session")
        

    def scan(self):
        self.image_count += 1
        self.camera.capture_file(self.current_session_dir + "/image" + str(self.image_count) + ".jpg")

    def stop_session(self):
        if self.is_in_session == True:
            self.is_in_session = False
            session_dir = self.current_session_dir
            self.current_session_dir = ""
            self.image_count = 0
            self.camera.stop()
        else:
            print("You must first start a scanning session")

        now = self.__get_datetime()
        return ScanSession(session_dir, now[0], now[1])



class ScanSession:
    directory_path = ""
    date = ""
    time = ""

    def __init__(self, directory_path, date, time):
        self.directory_path = directory_path
        self.date = date
        self.time = time

    def to_dict(self):
        return dict(directory_path = self.directory_path, date = self.date, time = self.time)

