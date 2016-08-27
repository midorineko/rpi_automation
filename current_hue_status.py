import sys
from qhue import Bridge
from rgb_cie import Converter
converter = Converter()

b = Bridge("100.66.30.18", "elbLovRPUcHaqss904iEJMH9LZrRwsvFeOKSfvOP")


strip_bri   = b.lights[1]()['state']['bri']
bloom_1_bri = b.lights[2]()['state']['bri']
bloom_2_bri = b.lights[3]()['state']['bri']

strip_xy   = b.lights[1]()['state']['xy']
bloom_1_xy = b.lights[2]()['state']['xy']
bloom_2_xy = b.lights[3]()['state']['xy']

strip_hex   = converter.CIE1931ToHex(strip_xy[0], strip_xy[1], bri=(strip_bri/254.0))
bloom_1_hex = converter.CIE1931ToHex(bloom_1_xy[0], bloom_1_xy[1], bri=(bloom_1_bri/254.0))
bloom_2_hex = converter.CIE1931ToHex(bloom_2_xy[0], bloom_2_xy[1], bri=(bloom_2_bri/254.0))

print(['hue', strip_bri, bloom_1_bri, bloom_2_bri, strip_hex, bloom_1_hex, bloom_2_hex])