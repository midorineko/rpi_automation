import RPi.GPIO as GPIO
import time
import pigpio
SERVO = 17

pi = pigpio.pi()

pi.set_servo_pulsewidth(SERVO, 1000)
time.sleep(1.53)
pi.set_servo_pulsewidth(SERVO, 1500)
