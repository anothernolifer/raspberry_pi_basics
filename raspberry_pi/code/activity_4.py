# set led state from user input 

import RPi.GPIO as GPIO
import time

LED_PIN = 17 

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

state = int(input("Enter 1 to turn ON the LED or 0 to turn OFF the LED: "))

if state == 1:
    GPIO.output(LED_PIN, GPIO.HIGH)

elif state == 0:
    GPIO.output(LED_PIN, GPIO.LOW)

else:
    print("Invalid input. Please enter 1 or 0.")
    GPIO.cleanup()
    exit


time.sleep(2) 
GPIO.cleanup()