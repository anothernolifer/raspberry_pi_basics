import machine
import time

BUTTON_PIN = 16
button = machine.Pin(BUTTON_PIN, machine.Pin.IN , machine.Pin.PULL_DOWN)


while True:
    print(button.value())
    time.sleep(0.1)