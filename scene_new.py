import sys
from qhue import Bridge
b = Bridge("100.66.30.18", "elbLovRPUcHaqss904iEJMH9LZrRwsvFeOKSfvOP")

lights = b.lights
print(b.config()['mac'])
print(b.lights())

state_1 = b.lights[1]()['state']['xy']
state_2 = b.lights[2]()['state']['xy']
state_3 = b.lights[3]()['state']['xy']


f = open("lights_main.py", "a")
f.write("elif command == '%s':" %sys.argv[-1] + "\n")
f.write("  b.lights(1, 'state', bri=255, on=True, xy=%s)" %state_1 + "\n")
f.write("  b.lights(2, 'state', bri=255, on=True, xy=%s)" %state_2 + "\n")
f.write("  b.lights(3, 'state', bri=255, on=True, xy=%s)" %state_3 + "\n")
f.close()


f = open("scene.txt", "a")
f.write(sys.argv[-1] + "\n")
f.close()