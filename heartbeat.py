# 
#  KevstahJr (kevstahjr.com)
#  Heartbeat.py
# 

import utime
from machine import Pin

# Declared Variables.
led_pin = Pin(25, Pin.OUT)
heartbeat_time = 0.5

print("Starting up Heartbeat...")
while True:
    led_pin.value(1)
    utime.sleep(heartbeat_time)
    led_pin.value(0)
    utime.sleep(heartbeat_time)
