# power_on_led_when_motion_detected

import RPi.GPIO as GPIO
import time

LED_PIN = 17
PIR_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(PIR_PIN, GPIO.IN , pull_up_down=GPIO.PUD_DOWN)
GPIO.output(LED_PIN, GPIO.LOW)

while True:
    time.sleep(0.1)
    if GPIO.input(PIR_PIN) == GPIO.HIGH:
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        GPIO.output(LED_PIN, GPIO.LOW)


GPIO.cleanup()