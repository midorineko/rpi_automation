import sys
import os
from qhue import Bridge
b = Bridge("192.168.0.101", "elbLovRPUcHaqss904iEJMH9LZrRwsvFeOKSfvOP")
lights = b.lights

command = sys.argv[-1]

if (command == 'led_off' or command == 'all_off' or command == 'off'):
	b.lights(1, 'state', on=False)
	b.lights(2, 'state', on=False)
	b.lights(3, 'state', on=False)
	b.lights(4, 'state', on=False)
elif command == 'led_on':
	b.lights(1, 'state', on=True)
	b.lights(2, 'state', on=True)
	b.lights(3, 'state', on=True)
	b.lights(4, 'state', on=True)
elif command == 'dota':
	b.lights(1, 'state', bri=255, on=True, xy=[0.6065, 0.3095])
	b.lights(2, 'state', bri=255, on=True, xy=[0.6883, 0.306])
	b.lights(3, 'state', bri=255, on=True, xy=[0.6883, 0.306])
	b.lights(4, 'state', bri=255, on=True, xy=[0.6065, 0.3095])
elif command == 'blaze':
	b.lights(1, 'state', bri=255, on=True, xy=[0.3344, 0.5002])
	b.lights(2, 'state', bri=255, on=True, xy=[0.3254, 0.5028])
	b.lights(3, 'state', bri=255, on=True, xy=[0.3239, 0.4932])
	b.lights(4, 'state', bri=255, on=True, xy=[0.3344, 0.5002])
elif command == 'chill':
	b.lights(1, 'state', bri=255, on=True, xy=[0.3069, 0.3152])
	b.lights(2, 'state', bri=255, on=True, xy=[0.3069, 0.3152])
	b.lights(3, 'state', bri=255, on=True, xy=[0.3069, 0.3152])
	b.lights(4, 'state', bri=255, on=True, xy=[0.3069, 0.3152])
elif command == 'sea_foam':
  b.lights(1, 'state', bri=255, on=True, xy=[0.1638, 0.3531])
  b.lights(2, 'state', bri=255, on=True, xy=[0.2263, 0.3402])
  b.lights(3, 'state', bri=255, on=True, xy=[0.1618, 0.3365])
  b.lights(4, 'state', bri=255, on=True, xy=[0.1638, 0.3531])
elif command == 'veg_box':
  b.lights(1, 'state', bri=255, on=True, xy=[0.3695, 0.168])
  b.lights(2, 'state', bri=255, on=True, xy=[0.3481, 0.156])
  b.lights(3, 'state', bri=255, on=True, xy=[0.3182, 0.1454])
  b.lights(4, 'state', bri=255, on=True, xy=[0.3695, 0.168])
elif command == 'kitty':
  b.lights(1, 'state', bri=254, on=True, xy=[0.3426, 0.1705])
  b.lights(2, 'state', bri=254, on=True, xy=[0.3949, 0.2899])
  b.lights(3, 'state', bri=254, on=True, xy=[0.2996, 0.2596])
  b.lights(4, 'state', bri=254, on=True, xy=[0.3426, 0.1705])
elif command == 'seattled':
  b.lights(1, 'state', bri=254, on=True, xy=[0.1957, 0.1006])
  b.lights(2, 'state', bri=254, on=True, xy=[0.3037, 0.2383])
  b.lights(3, 'state', bri=254, on=True, xy=[0.3088, 0.2531])
  b.lights(4, 'state', bri=254, on=True, xy=[0.1722, 0.0567])
elif command == 'california_springtime':
  b.lights(1, 'state', bri=254, on=True, xy=[0.1719, 0.112])
  b.lights(2, 'state', bri=254, on=True, xy=[0.3136, 0.1438])
  b.lights(3, 'state', bri=254, on=True, xy=[0.1982, 0.3208])
  b.lights(4, 'state', bri=254, on=True, xy=[0.4858, 0.2777])
elif command == 'blooming_heaven':
  b.lights(1, 'state', bri=254, on=True, xy=[0.2076, 0.1057])
  b.lights(2, 'state', bri=254, on=True, xy=[0.2956, 0.2372])
  b.lights(3, 'state', bri=254, on=True, xy=[0.2555, 0.3274])
  b.lights(4, 'state', bri=254, on=True, xy=[0.2564, 0.145])
elif command == 'morning':
  b.lights(1, 'state', bri=254, on=True, xy=[0.3342, 0.3605])
  b.lights(2, 'state', bri=254, on=True, xy=[0.3342, 0.3605])
  b.lights(3, 'state', bri=254, on=True, xy=[0.3342, 0.3605])
  b.lights(4, 'state', bri=254, on=True, xy=[0.3538, 0.3794])
  os.system("python blinds_open.py")
elif command == 'blue_raspberry':
  b.lights(1, 'state', bri=254, on=True, xy=[0.3564, 0.159])
  b.lights(2, 'state', bri=254, on=True, xy=[0.3442, 0.2055])
  b.lights(3, 'state', bri=254, on=True, xy=[0.2228, 0.348])
  b.lights(4, 'state', bri=254, on=True, xy=[0.1611, 0.3529])
elif command == 'hawaiian_sun_set':
  b.lights(1, 'state', bri=254, on=True, xy=[0.6903, 0.3074])
  b.lights(2, 'state', bri=254, on=True, xy=[0.5878, 0.4001])
  b.lights(3, 'state', bri=254, on=True, xy=[0.5019, 0.4751])
  b.lights(4, 'state', bri=254, on=True, xy=[0.4953, 0.4368])
elif command == 'seahawks':
  b.lights(1, 'state', bri=254, on=True, xy=[0.1637, 0.3522])
  b.lights(2, 'state', bri=254, on=True, xy=[0.169, 0.1308])
  b.lights(3, 'state', bri=254, on=True, xy=[0.1497, 0.1939])
  b.lights(4, 'state', bri=254, on=True, xy=[0.2344, 0.5274])
elif command == 'gaming':
  b.lights(1, 'state', bri=254, on=True, xy=[0.6064, 0.3085])
  b.lights(2, 'state', bri=254, on=True, xy=[0.6883, 0.3065])
  b.lights(3, 'state', bri=254, on=True, xy=[0.6883, 0.3065])
  b.lights(4, 'state', bri=254, on=True, xy=[0.6066, 0.3095])
elif command == 'night_smoke':
  b.lights(1, 'state', bri=1, on=True, xy=[0.3333, 0.5004])
  b.lights(2, 'state', bri=160, on=True, xy=[0.3243, 0.5028])
  b.lights(3, 'state', bri=1, on=True, xy=[0.3229, 0.493])
  b.lights(4, 'state', bri=1, on=True, xy=[0.3343, 0.5005])
elif command == 'night':
  b.lights(1, 'state', on=False)
  b.lights(2, 'state', on=False)
  b.lights(3, 'state', on=False)
  b.lights(4, 'state', on=False)
  os.system('python blinds_close.py')
elif command == 'ice':
  b.lights(1, 'state', bri=254, on=True, xy=[0.3048, 0.3149])
  b.lights(2, 'state', bri=254, on=True, xy=[0.3069, 0.3152])
  b.lights(3, 'state', bri=254, on=True, xy=[0.3048, 0.3149])
  b.lights(4, 'state', bri=254, on=True, xy=[0.3073, 0.3156])
  os.system('python blinds_close.py')
elif command == 'kitty_combo':
  b.lights(1, 'state', bri=223, on=True, xy=[0.1638, 0.3531])
  b.lights(2, 'state', bri=166, on=True, xy=[0.2318, 0.3403])
  b.lights(3, 'state', bri=100, on=True, xy=[0.1618, 0.3365])
  b.lights(4, 'state', bri=254, on=True, xy=[0.3426, 0.1703])
  os.system('python blinds_close.py')
elif command == 'grapevine':
  b.lights(1, 'state', bri=173, on=True, xy=[0.1639, 0.3533])
  b.lights(2, 'state', bri=101, on=True, xy=[0.6515, 0.3437])
  b.lights(3, 'state', bri=88, on=True, xy=[0.141, 0.1122])
  b.lights(4, 'state', bri=114, on=True, xy=[0.2508, 0.0948])
  os.system('python blinds_close.py')
elif command == 'purple_rain':
  b.lights(1, 'state', bri=254, on=True, xy=[0.2084, 0.1061])
  b.lights(2, 'state', bri=254, on=True, xy=[0.1658, 0.0908])
  b.lights(3, 'state', bri=254, on=True, xy=[0.1658, 0.0908])
  b.lights(4, 'state', bri=254, on=True, xy=[0.2283, 0.1202])
  os.system('python blinds_open.py')
