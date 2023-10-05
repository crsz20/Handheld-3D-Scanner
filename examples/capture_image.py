from picamera2 import Picamera2, Preview
import time
picam2 = Picamera2()
camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
picam2.configure(camera_config)
# with direct display:
#picam2.start_preview(Preview.QTGL)
# with remote vnc viewing:
picam2.start_preview(Preview.QT)
picam2.start()
time.sleep(2)
picam2.capture_file("/home/crsz/Pictures/Scans/test_picam2.jpg")