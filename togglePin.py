import machine                                      # Main Lib to work with ESP in micropython
import time                                         # Lib to delay
from machine import Pin                             # For select pins

led = machine.Pin(2, machine.Pin.OUT)               # Standard onboard led pin

def toggle(p):
    p.value(not p.value())

while True:
    toggle(led)
    time.sleep(1)