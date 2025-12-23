# use_function_to_change_powered_on_led_when_pressing_button

import machine
import time

LED_PIN_LIST = [2, 15, 17]
BUTTON_PIN = 16

leds = [machine.Pin(pin, machine.Pin.OUT) for pin in LED_PIN_LIST]
button = machine.Pin(BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)

def power_on_selected_led_only(index):
    for i in range(len(leds)):
        if i == index:
            leds[i].value(1)
        else:
            leds[i].value(0)

for led in leds:
    led.value(0)

previous_button_state = button.value()
led_index = 0

while True:
    time.sleep(0.01)
    button_state = button.value()
    if button_state != previous_button_state:
        previous_button_state = button_state
        if button_state == 1:
            power_on_selected_led_only(led_index)
            led_index += 1
            if led_index >= len(leds):
                led_index = 0