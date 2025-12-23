# change powered on led when pressing button

import machine
import time

LED_1_PIN = 2
LED_2_PIN = 15
LED_3_PIN = 17
BUTTON_PIN = 16

led1 = machine.Pin(LED_1_PIN, machine.Pin.OUT)
led2 = machine.Pin(LED_2_PIN, machine.Pin.OUT)
led3 = machine.Pin(LED_3_PIN, machine.Pin.OUT)
button = machine.Pin(BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)

led1.value(0)
led2.value(0)
led3.value(0)

previous_button_state = button.value()
led_index = 0

while True:
    time.sleep(0.01)
    button_state = button.value()
    if button_state != previous_button_state:
        previous_button_state = button_state
        if button_state == 1:
            if led_index == 0:
                led1.value(1)
                led2.value(0)
                led3.value(0)
                led_index = 1
            elif led_index == 1:
                led1.value(0)
                led2.value(1)
                led3.value(0)
                led_index = 2
            else:
                led1.value(0)
                led2.value(0)
                led3.value(1)
                led_index = 0