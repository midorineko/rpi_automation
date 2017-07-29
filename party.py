import sys
import time
import os
from qhue import Bridge

f = open("hue_id.txt", "r")
hue_id = f.readlines()[-1].rstrip()
f.close()

b = Bridge(hue_id, "elbLovRPUcHaqss904iEJMH9LZrRwsvFeOKSfvOP")
lights = b.lights

command = sys.argv[-1]


b.lights(1, 'state', bri=255, on=True, xy=[0.6065, 0.3095])
b.lights(2, 'state', bri=255, on=True, xy=[0.6883, 0.306])
b.lights(3, 'state', bri=255, on=True, xy=[0.6883, 0.306])
b.lights(4, 'state', bri=255, on=True, xy=[0.6065, 0.3095])
time.sleep(0.25)

b.lights(1, 'state', bri=255, on=True, xy=[0.3344, 0.5002])
b.lights(2, 'state', bri=255, on=True, xy=[0.3254, 0.5028])
b.lights(3, 'state', bri=255, on=True, xy=[0.3239, 0.4932])
b.lights(4, 'state', bri=255, on=True, xy=[0.3344, 0.5002])
time.sleep(0.25)

b.lights(1, 'state', bri=255, on=True, xy=[0.3069, 0.3152])
b.lights(2, 'state', bri=255, on=True, xy=[0.3069, 0.3152])
b.lights(3, 'state', bri=255, on=True, xy=[0.3069, 0.3152])
b.lights(4, 'state', bri=255, on=True, xy=[0.3069, 0.3152])
time.sleep(0.25)

b.lights(1, 'state', bri=255, on=True, xy=[0.1638, 0.3531])
b.lights(2, 'state', bri=255, on=True, xy=[0.2263, 0.3402])
b.lights(3, 'state', bri=255, on=True, xy=[0.1618, 0.3365])
b.lights(4, 'state', bri=255, on=True, xy=[0.1638, 0.3531])
time.sleep(0.25)

b.lights(1, 'state', bri=255, on=True, xy=[0.1638, 0.3531])
b.lights(2, 'state', bri=255, on=True, xy=[0.2263, 0.3402])
b.lights(3, 'state', bri=255, on=True, xy=[0.1618, 0.3365])
b.lights(4, 'state', bri=255, on=True, xy=[0.1638, 0.3531])
