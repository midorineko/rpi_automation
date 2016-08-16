import time
import datetime
import os

f = open("/home/pi/rpi_automation/water.txt", "r")
last_line = f.readlines()[-1]
f.close()

start_date = time.strftime("%d/%m/%Y")
start_hour = time.strftime("%H:%M:%S")

last_line = last_line.rstrip().replace("'", "").replace("[","").replace("]","")
last_date = last_line.split(",")[0]

todays_date = time.strftime("%d/%m/%Y")

last_date_final = datetime.datetime.strptime(last_date, '%d/%m/%Y')
todays_date_final = datetime.datetime.strptime(todays_date, '%d/%m/%Y')

last_date_plus_three = last_date_final + datetime.timedelta(days=3)

if last_date_plus_three == todays_date_final:
   os.system("python /home/pi/rpi_automation/TransmitRF.py c_on")
   time.sleep(45)
   os.system("python /home/pi/rpi_automation/TransmitRF.py c_off")
   final = [start_date, start_hour, time.strftime("%H:%M:%S"), '45']
   final_string = '%s' %final
   f = open("/home/pi/rpi_automation/water.txt", "a")
   f.write(final_string + "\n")
   f.close()

