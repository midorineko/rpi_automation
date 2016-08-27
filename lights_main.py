import sys
from qhue import Bridge
b = Bridge("100.66.30.18", "elbLovRPUcHaqss904iEJMH9LZrRwsvFeOKSfvOP")
lights = b.lights

command = sys.argv[-1]

if command == 'led_off':
	b.lights(1, 'state', on=False)
	b.lights(2, 'state', on=False)
	b.lights(3, 'state', on=False)
elif command == 'led_on':
	b.lights(1, 'state', on=True)
	b.lights(2, 'state', on=True)
	b.lights(3, 'state', on=True)
elif command == 'all_off':
	b.lights(1, 'state', on=False)
	b.lights(2, 'state', on=False)
	b.lights(3, 'state', on=False)
elif command == 'dota':
	b.lights(1, 'state', bri=255, on=True, xy=[0.6065, 0.3095])
	b.lights(2, 'state', bri=255, on=True, xy=[0.6883, 0.306])
	b.lights(3, 'state', bri=255, on=True, xy=[0.6883, 0.306])
elif command == 'blaze':
	b.lights(1, 'state', bri=255, on=True, xy=[0.3344, 0.5002])
	b.lights(2, 'state', bri=255, on=True, xy=[0.3254, 0.5028])
	b.lights(3, 'state', bri=255, on=True, xy=[0.3239, 0.4932])
elif command == 'chill':
	b.lights(1, 'state', bri=255, on=True, xy=[0.3069, 0.3152])
	b.lights(2, 'state', bri=255, on=True, xy=[0.3069, 0.3152])
	b.lights(3, 'state', bri=255, on=True, xy=[0.3069, 0.3152])
elif command == 'off':
	b.lights(1, 'state', bri=255, on=False)
	b.lights(2, 'state', bri=255, on=False)
	b.lights(3, 'state', bri=255, on=False)
elif command == 'seafoam':
  b.lights(1, 'state', bri=255, on=True, xy=[0.1638, 0.3531])
  b.lights(2, 'state', bri=255, on=True, xy=[0.2263, 0.3402])
  b.lights(3, 'state', bri=255, on=True, xy=[0.1618, 0.3365])
elif command == 'veg_box':
  b.lights(1, 'state', bri=255, on=True, xy=[0.3695, 0.168])
  b.lights(2, 'state', bri=255, on=True, xy=[0.3481, 0.156])
  b.lights(3, 'state', bri=255, on=True, xy=[0.3182, 0.1454])
elif command == 'kitty':
  b.lights(1, 'state', bri=254, on=True, xy=[0.3426, 0.1705])
  b.lights(2, 'state', bri=254, on=True, xy=[0.3949, 0.2899])
  b.lights(3, 'state', bri=254, on=True, xy=[0.2996, 0.2596])
