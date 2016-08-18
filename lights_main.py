import sys
from qhue import Bridge
b = Bridge("100.66.30.18", "elbLovRPUcHaqss904iEJMH9LZrRwsvFeOKSfvOP")
lights = b.lights
print(b.config()['mac'])
print(b.lights())

command = sys.argv[-1]

if command == 'led_off':
	b.lights(1, 'state', bri=255, on=False)
	b.lights(2, 'state', bri=255, on=False)
	b.lights(3, 'state', bri=255, on=False)
elif command == 'led_on':
	b.lights(1, 'state', bri=255, on=True)
	b.lights(2, 'state', bri=255, on=True)
	b.lights(3, 'state', bri=255, on=True)
elif command == 'dota':
	b.lights(1, 'state', bri=255, on=True, xy=[0.6065, 0.3095])
	b.lights(2, 'state', bri=255, on=True, xy=[0.6883, 0.306])
	b.lights(3, 'state', bri=255, on=True, xy=[0.6883, 0.306])
	os.system("python /home/pi/rpi_automation/livolo.py off")
elif command == 'blaze':
	b.lights(1, 'state', bri=255, on=True, xy=[0.3344, 0.5002])
	b.lights(2, 'state', bri=255, on=True, xy=[0.3254, 0.5028])
	b.lights(3, 'state', bri=255, on=True, xy=[0.3239, 0.4932])
	os.system("python /home/pi/rpi_automation/livolo.py off")
elif command == 'chill':
	b.lights(1, 'state', bri=255, on=True, xy=[0.3069, 0.3152])
	b.lights(2, 'state', bri=255, on=True, xy=[0.3069, 0.3152])
	b.lights(3, 'state', bri=255, on=True, xy=[0.3069, 0.3152])
	os.system("python /home/pi/rpi_automation/livolo.py off")
elif command == 'off':
	b.lights(1, 'state', bri=255, on=False)
	b.lights(2, 'state', bri=255, on=False)
	b.lights(3, 'state', bri=255, on=False)
	os.system("python /home/pi/rpi_automation/livolo.py off")
elif command == 'on':
	os.system("python /home/pi/rpi_automation/livolo.py on")
elif command == 'seafoam':
  b.lights(1, 'state', bri=255, on=True, xy=[0.1638, 0.3531])
  b.lights(2, 'state', bri=255, on=True, xy=[0.2263, 0.3402])
  b.lights(3, 'state', bri=255, on=True, xy=[0.1618, 0.3365])
  os.system("python /home/pi/rpi_automation/livolo.py off")
elif command == 'veg_box':
  b.lights(1, 'state', bri=255, on=True, xy=[0.3695, 0.168])
  b.lights(2, 'state', bri=255, on=True, xy=[0.3481, 0.156])
  b.lights(3, 'state', bri=255, on=True, xy=[0.3182, 0.1454])
  os.system("python /home/pi/rpi_automation/livolo.py off")
