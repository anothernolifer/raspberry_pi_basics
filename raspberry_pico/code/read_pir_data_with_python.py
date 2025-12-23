# read_pir_data_with_python

import machine
import time

PIR_PIN = 20   

pir = machine.Pin(PIR_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    print(pir.value())
    time.sleep(0.1)