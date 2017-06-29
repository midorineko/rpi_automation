import sys
from qhue import Bridge
b = Bridge("192.168.0.101", "elbLovRPUcHaqss904iEJMH9LZrRwsvFeOKSfvOP")

lights = b.lights

state_1 = b.lights[1]()['state']
state_2 = b.lights[2]()['state']
state_3 = b.lights[3]()['state']
state_4 = b.lights[4]()['state']

p = open("blinds.txt", "r")
last_line = p.readlines()[-1].rstrip()
p.close()

f = open("scene_main.py", "a")
f.write("elif command == '%s':" %sys.argv[-1] + "\n")

if state_1['on'] == False:
   f.write("  b.lights(1, 'state', on=False)" "\n")
else:
   f.write("  b.lights(1, 'state', bri=%s, on=True, xy=%s)" %(state_1['bri'], state_1['xy']) + "\n")

if state_2['on'] == False:
   f.write("  b.lights(2, 'state', on=False)" "\n")
else:
   f.write("  b.lights(2, 'state', bri=%s, on=True, xy=%s)" %(state_2['bri'], state_2['xy']) + "\n")

if state_3['on'] == False:
   f.write("  b.lights(3, 'state', on=False)" "\n")
else:
   f.write("  b.lights(3, 'state', bri=%s, on=True, xy=%s)" %(state_3['bri'], state_3['xy']) + "\n")

if state_4['on'] == False:
   f.write("  b.lights(4, 'state', on=False)" "\n")
else:
   f.write("  b.lights(4, 'state', bri=%s, on=True, xy=%s)" %(state_4['bri'], state_4['xy']) + "\n")

f.write("  os.system('python blinds_%s.py')" %(last_line) + "\n")

f.close()


f = open("scene.txt", "a")
f.write(sys.argv[-1] + "\n")
f.close()
