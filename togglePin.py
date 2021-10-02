import machine
import time
from machine import Pin

def toggle(p):
    p.value(not p.value())