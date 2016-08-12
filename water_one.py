import time
import sys

f = open('water.txt','a')

start_date = time.strftime("%d/%m/%Y")
start_hour = time.strftime("%H:%M:%S")

time.sleep(int(float(sys.argv[-1])))

print([start_date, start_hour, time.strftime("%H:%M:%S"), sys.argv[-1]], file=f)

f.close()