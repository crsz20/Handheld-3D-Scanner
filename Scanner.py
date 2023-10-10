# External Dependencies
import os
from datetime import datetime
from dateutil import tz
from picamera2 import Picamera2

# Handles taking a photo and controlling system
# state. Then, hands the filepath + date to the database
class Scanner:
    root_dir = ""
    current_session_dir = ""
    camera = Picamera2()
    ## TODO: initialize accelerometer

    def __init__(self, root_dir):
        self.root_dir = root_dir

    def __get_datetime__(self):
        now = datetime.now()
        timestamp = datetime.utcfromtimestamp(now.timestamp())
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


    def start_session(self):
        session_num = 1
        
        while True:
            session_path = os.path.join(self.root_dir, "session" + str(session_num))
            if not os.path.exists(session_path):
                break
            
            session_num += 1
        
        os.mkdir(session_path)
        self.current_session_dir = session_path
        self.camera.start()
        

    def scan(self):
        # TODO: validate that a session has started
        # TODO: take a series of pictures
        print("hi")

    def stop_session(self):
        # TODO: validate that session has started
        # TODO: stop the camera
        session_dir = self.current_session_dir
        self.current_session_dir = ""
        self.camera.stop()

        now = self.__get_datetime__()
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

