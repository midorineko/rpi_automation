import sys
import os

f = open("scene_main_new.txt", "a")
f.write(sys.argv[-1] + "=" + sys.argv[-2] + "\n")
f.close()