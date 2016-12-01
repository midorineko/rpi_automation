import sys
from qhue import Bridge
from rgb_cie import Converter
b = Bridge("192.168.0.100", "elbLovRPUcHaqss904iEJMH9LZrRwsvFeOKSfvOP")
lights = b.lights
converter = Converter()

b.lights(1, 'state', on=True, xy=converter.hexToCIE1931(sys.argv[-4]))
b.lights(2, 'state', on=True, xy=converter.hexToCIE1931(sys.argv[-3]))
b.lights(3, 'state', on=True, xy=converter.hexToCIE1931(sys.argv[-2]))
b.lights(4, 'state', on=True, xy=converter.hexToCIE1931(sys.argv[-1]))
