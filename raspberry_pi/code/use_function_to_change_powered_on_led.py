# use_function_to_change_powered_on_led_when_pressing_button

import RPi.GPIO as GPIO
import time


LED_PIN_LIST = [17, 27, 22]
BUTTON_PIN = 26

def power_on_selected_led_only(selected_led_pin):
    if selected_led_pin not in LED_PIN_LIST:
        return
    for led_pin in LED_PIN_LIST:
        if led_pin == selected_led_pin:
            GPIO.output(led_pin, GPIO.HIGH)
        else:
            GPIO.output(led_pin, GPIO.LOW)


GPIO.setmode(GPIO.BCM)

for led_pin in LED_PIN_LIST:
    GPIO.setup(pin, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN)


for led_pin in LED_PIN_LIST:
    GPIO.output(led_pin, GPIO.LOW)

previous_button_state = GPIO.input(BUTTON_PIN)
led_index = 0


while True:
    time.sleep(0.01)
    buttom_state = GPIO.input(BUTTON_PIN)
    if buttom_state != previous_button_state:
        previous_button_state = buttom_state
        if buttom_state == GPIO.HIGH:
            power_on_selected_led_only(LED_PIN_LIST[led_index])
            led_index += 1

            if led_index >= len(LED_PIN_LIST):
                led_index = 0

GPIO.cleanup()
