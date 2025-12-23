import machine
import time

LED_PIN = 2
BUTTON_PIN = 16

led = machine.Pin(LED_PIN, machine.Pin.OUT)
button = machine.Pin(BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        led.value(1)
    else:
        led.value(0)
    time.sleep(0.01)