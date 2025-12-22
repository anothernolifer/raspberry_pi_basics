# set led state from user input 


from machine import Pin
import time

LED_PIN = 2

led = Pin(LED_PIN, Pin.OUT)

state = int(input("Enter 1 to turn ON the LED or 0 to turn OFF the LED: "))

if state == 1:
    led.value(1)
elif state == 0:
    led.value(0)
else:
    print("Invalid input. Please enter 1 or 0.")

time.sleep(2)
led.value(0)
