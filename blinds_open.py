import RPi.GPIO as GPIO
import time
import pigpio
import os

f = open("blinds.txt", "r")
last_line = f.readlines()[-1].rstrip()
f.close()

if last_line == 'close':
  f = open("blinds.txt", "w")
  f.write('open' + "\n")
  f.close()
  SERVO = 17
  pi = pigpio.pi()
  pi.set_servo_pulsewidth(SERVO, 2000)
  time.sleep(1.53)
  pi.set_servo_pulsewidth(SERVO, 1500)
