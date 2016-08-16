import time
import sys
import os

f = open('/home/pi/rpi_automation/water.txt','a')

start_date = time.strftime("%d/%m/%Y")
start_hour = time.strftime("%H:%M:%S")

os.system("python /home/pi/rpi_automation/TransmitRF.py c_on")
   
time.sleep(int(float(sys.argv[-1])))

os.system("python /home/pi/rpi_automation/TransmitRF.py c_off")

final = [start_date, start_hour, time.strftime("%H:%M:%S"), sys.argv[-1]]
final_string = '%s' %final
f.write(final_string + "\n")

f.close()
