import time
import datetime

f = open("water.txt", "r")
last_line = f.readlines()[-1]
f.close

last_line = last_line.rstrip().replace("'", "").replace("[","").replace("]","")
last_date = last_line.split(",")[0]

todays_date = time.strftime("%d/%m/%Y")

last_date_final = datetime.datetime.strptime(last_date, '%d/%m/%Y')
todays_date_final = datetime.datetime.strptime(todays_date, '%d/%m/%Y')

last_date_plus_three = last_date_final + datetime.timedelta(days=3)

if last_date_plus_three == todays_date_final:
   print("Water Today!")
else:
   print("No no not today")
