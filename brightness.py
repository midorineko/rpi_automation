import sys
from qhue import Bridge
b = Bridge("192.168.0.102", "elbLovRPUcHaqss904iEJMH9LZrRwsvFeOKSfvOP")
lights = b.lights

brightness = int(sys.argv[-1])

print(int(sys.argv[-1]))


if len(sys.argv) < 3:
	if brightness < 1:
		b.lights(1, 'state', on=False)
		b.lights(2, 'state', on=False)
		b.lights(3, 'state', on=False)
		b.lights(4, 'state', on=False)
	else:
		if brightness > 255:
			brightness = 255
		b.lights(1, 'state', bri=brightness, on=True)
		b.lights(2, 'state', bri=brightness, on=True)
		b.lights(3, 'state', bri=brightness, on=True)
		b.lights(4, 'state', bri=brightness, on=True)
else:
	strip_bri = int(sys.argv[-4])/100. * 255
	bloom1_bri = int(sys.argv[-3])/100. * 255
	bloom2_bri = int(sys.argv[-2])/100. * 255
	strip2_bri = int(sys.argv[-1])/100. * 255
	b.lights(1, 'state', bri=int(strip_bri), on=True)
	b.lights(2, 'state', bri=int(bloom1_bri), on=True)
	b.lights(3, 'state', bri=int(bloom2_bri), on=True)
	b.lights(4, 'state', bri=int(strip2_bri), on=True)
	if strip_bri < 1:
		b.lights(1, 'state', on=False)
	if bloom1_bri < 1:
		b.lights(2, 'state', on=False)
	if bloom2_bri < 1:
		b.lights(3, 'state', on=False)
	if strip2_bri < 1:
		b.lights(4, 'state', on=False)
