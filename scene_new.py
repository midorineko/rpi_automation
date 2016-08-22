import sys
from qhue import Bridge
b = Bridge("100.66.30.18", "elbLovRPUcHaqss904iEJMH9LZrRwsvFeOKSfvOP")

lights = b.lights

state_1 = b.lights[1]()['state']
state_2 = b.lights[2]()['state']
state_3 = b.lights[3]()['state']

f = open("lights_main.py", "a")
f.write("elif command == '%s':" %sys.argv[-1] + "\n")

f.write("  b.lights(1, 'state', bri=%s, on=True, xy=%s)" %(state_1['bri'], state_1['xy']) + "\n")
f.write("  b.lights(2, 'state', bri=%s, on=True, xy=%s)" %(state_2['bri'], state_2['xy']) + "\n")
f.write("  b.lights(3, 'state', bri=%s, on=True, xy=%s)" %(state_3['bri'], state_3['xy']) + "\n")

f.close()


f = open("scene.txt", "a")
f.write(sys.argv[-1] + "\n")
f.close()
