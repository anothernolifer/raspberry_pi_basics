# take_photo_from_raspberry_pi_camera 

from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution = (1024, 768)  # set resolution
camera.rotation = 180  # rotate camera if needed
time.sleep(2)  # allow camera to warm up

file_name = "/home/pi/camera/file_name.jpg"
camera.capture(file_name)
print(f"Photo saved to {file_name}")
