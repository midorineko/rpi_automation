import sys
from qhue import Bridge
from rgb_cie import Converter
b = Bridge("100.66.30.18", "elbLovRPUcHaqss904iEJMH9LZrRwsvFeOKSfvOP")
lights = b.lights
converter = Converter()

b.lights(1, 'state', bri=255, on=True, xy=converter.hexToCIE1931(sys.argv[-3]))
b.lights(2, 'state', bri=255, on=True, xy=converter.hexToCIE1931(sys.argv[-2]))
b.lights(3, 'state', bri=255, on=True, xy=converter.hexToCIE1931(sys.argv[-1]))