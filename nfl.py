import nflgame
import time
import sys
from qhue import Bridge
b = Bridge("192.168.0.100", "elbLovRPUcHaqss904iEJMH9LZrRwsvFeOKSfvOP")
lights = b.lights


stupidest_var=""
year, week = nflgame.live.current_year_and_week()
while True:
    games = nflgame.games(year, week)
    for p in games:
       if p.nice_score().encode('ascii','ignore').find('SEA') > -1:
          stupid_var = p.nice_score().encode('ascii','ignore').split(" ")
          stupid_var2 = stupid_var.index('SEA') + 1
          stupid_var3 = stupid_var[stupid_var2]
          if stupidest_var == stupid_var3:
            print p
            print "we didn't"
            print stupidest_var
          elif stupidest_var != stupid_var3:
            stupidest_var = stupid_var3
            print 'we did it'
            print stupidest_var
            b.lights(1, 'state', on=True)
            b.lights(2, 'state', on=True)
            b.lights(3, 'state', on=True)
            b.lights(4, 'state', on=True)
            b.lights(1, 'state', bri=255, on=True, xy=[0.6065, 0.3095])
            b.lights(2, 'state', bri=255, on=True, xy=[0.6883, 0.306])
            b.lights(3, 'state', bri=255, on=True, xy=[0.6883, 0.306])
            b.lights(4, 'state', bri=255, on=True, xy=[0.6065, 0.3095])
            b.lights(1, 'state', bri=255, on=True, xy=[0.3344, 0.5002])
            b.lights(2, 'state', bri=255, on=True, xy=[0.3254, 0.5028])
            b.lights(3, 'state', bri=255, on=True, xy=[0.3239, 0.4932])
            b.lights(4, 'state', bri=255, on=True, xy=[0.3344, 0.5002])
            b.lights(1, 'state', bri=255, on=True, xy=[0.3069, 0.3152])
            b.lights(2, 'state', bri=255, on=True, xy=[0.3069, 0.3152])
            b.lights(3, 'state', bri=255, on=True, xy=[0.3069, 0.3152])
            b.lights(4, 'state', bri=255, on=True, xy=[0.3069, 0.3152])
            b.lights(1, 'state', bri=255, on=True, xy=[0.1638, 0.3531])
            b.lights(2, 'state', bri=255, on=True, xy=[0.2263, 0.3402])
            b.lights(3, 'state', bri=255, on=True, xy=[0.1618, 0.3365])
            b.lights(4, 'state', bri=255, on=True, xy=[0.1638, 0.3531])
            b.lights(1, 'state', bri=255, on=True, xy=[0.1638, 0.3531])
            b.lights(2, 'state', bri=255, on=True, xy=[0.2263, 0.3402])
            b.lights(3, 'state', bri=255, on=True, xy=[0.1618, 0.3365])
            b.lights(4, 'state', bri=255, on=True, xy=[0.1638, 0.3531])
    time.sleep(10)

