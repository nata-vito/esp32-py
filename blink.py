import machine                                      # Main Lib to work with ESP in micropython
import time                                         # Lib to delay
from machine import Pin                             # For select pins

led = machine.Pin(2, machine.Pin.OUT)               # Standar on board led pin

def blink():
    while True:
        led.value(1)            # Turn led on
        time.sleep(1)           # Delay
        led.value(0)            # Turn led off
        time.sleep(1)

        
blink()
