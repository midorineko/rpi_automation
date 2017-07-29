import sys
import os
from qhue import Bridge
from rgb_cie import Converter

f = open("hue_id.txt", "r")
hue_id = f.readlines()[-1].rstrip()
f.close()

b = Bridge(hue_id, "elbLovRPUcHaqss904iEJMH9LZrRwsvFeOKSfvOP")
lights = b.lights
converter = Converter()

b.lights(1, 'state', on=True, xy=converter.hexToCIE1931(sys.argv[-4]))
b.lights(2, 'state', on=True, xy=converter.hexToCIE1931(sys.argv[-3]))
b.lights(3, 'state', on=True, xy=converter.hexToCIE1931(sys.argv[-2]))
b.lights(4, 'state', on=True, xy=converter.hexToCIE1931(sys.argv[-1]))
