# power_on_led_when_motion_detected

import machine
import time

LED_PIN = 2
PIR_PIN = 20

led = machine.Pin(LED_PIN, machine.Pin.OUT)
pir = machine.Pin(PIR_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)

led.value(0)

while True:
    time.sleep(0.1)
    if pir.value() == 1:
        led.value(1)
    else:
        led.value(0)