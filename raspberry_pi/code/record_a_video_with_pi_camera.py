# record_a_video_with_pi_camera

import time
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)  # set resolution
camera.rotation = 180  # rotate camera if needed
time.sleep(2)  # allow camera to warm up

file_name = "/home/pi/camera/file_name.h264"
camera.start_recording(file_name)
camera.wait_recording(10)  # record for 10 seconds
camera.stop_recording()
print(f"Video saved to {file_name}")