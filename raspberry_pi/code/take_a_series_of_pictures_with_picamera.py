# take_a_series_of_pictures_with_picamera

import os
from picamera import PiCamera
import time

FOLDER_NAME = "/home/pi/folder_name"

if not os.path.exists(FOLDER_NAME):
    os.mkdir(FOLDER_NAME)        

camera = PiCamera()
camera.resolution = (1024, 768)
camera.rotation = 180
time.sleep(2) 

counter = 1


while True:
    file_name = FOLDER_NAME + "/img"+str(counter) +".jpg"
    counter += 1
    camera.capture(file_name)
    print("Captured " + file_name)
    time.sleep(5)
