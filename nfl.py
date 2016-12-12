import nflgame
import time
import sys
import sys
from qhue import Bridge
b = Bridge("192.168.0.102", "elbLovRPUcHaqss904iEJMH9LZrRwsvFeOKSfvOP")
lights = b.lights

suck_team = ""
stupidest_var=""
sea_score = 0
sea_score_last = 0
suck_score = 0
suck_score_last = 0
game_on = True
winning_team = ''
current_score = ''
event_plays=[]

class C:
    def score_method(self, sea_score, sea_score_last, suck_score, suck_score_last):
        b.lights(1, 'state', bri=255, on=True, xy=[0.6065, 0.3095])
        b.lights(2, 'state', bri=255, on=True, xy=[0.6883, 0.306])
        b.lights(3, 'state', bri=255, on=True, xy=[0.6883, 0.306])
        b.lights(4, 'state', bri=255, on=True, xy=[0.6065, 0.3095])
        b.lights(1, 'state', bri=255, on=True, xy=[0.3344, 0.5002])
        b.lights(2, 'state', bri=255, on=True, xy=[0.3254, 0.5028])
        b.lights(3, 'state', bri=255, on=True, xy=[0.3239, 0.4932])
        b.lights(4, 'state', bri=255, on=True, xy=[0.3344, 0.5002])
        b.lights(1, 'state', bri=255, on=True, xy=[0.3344, 0.5002])
        b.lights(2, 'state', bri=255, on=True, xy=[0.3254, 0.5028])
        b.lights(3, 'state', bri=255, on=True, xy=[0.3239, 0.4932])
        b.lights(4, 'state', bri=255, on=True, xy=[0.3344, 0.5002])
        b.lights(1, 'state', bri=255, on=True, xy=[0.1638, 0.3531])
        b.lights(2, 'state', bri=255, on=True, xy=[0.2263, 0.3402])
        b.lights(3, 'state', bri=255, on=True, xy=[0.1618, 0.3365])
        b.lights(4, 'state', bri=255, on=True, xy=[0.1638, 0.3531])
        b.lights(1, 'state', bri=255, on=True, xy=[0.1638, 0.3531])
        b.lights(2, 'state', bri=255, on=True, xy=[0.2263, 0.3402])
        b.lights(3, 'state', bri=255, on=True, xy=[0.1618, 0.3365])
        b.lights(4, 'state', bri=255, on=True, xy=[0.1638, 0.3531])
        b.lights(1, 'state', bri=255, on=False)
        b.lights(2, 'state', bri=255, on=False)
        b.lights(3, 'state', bri=255, on=False)
        b.lights(4, 'state', bri=255, on=False)
        if int(sea_score) != int(sea_score_last):
            score_diff = int(sea_score) - int(sea_score_last)
            print("Good :)")
            b.lights(2, 'state', bri=255, on=True, xy=[0.1497, 0.1939])
            b.lights(3, 'state', bri=255, on=True, xy=[0.1497, 0.1939])
        else:
            score_diff = int(suck_score) - int(suck_score_last)
            print("Bad :(")
            b.lights(2, 'state', bri=255, on=True, xy=[0.6883, 0.306])
            b.lights(3, 'state', bri=255, on=True, xy=[0.6883, 0.306])
        if score_diff == 2:
            print("Safety or two point conversion!")
            b.lights(1, 'state', bri=255, on=True, xy=[0.3538, 0.3794])
            b.lights(4, 'state', bri=255, on=True, xy=[0.3538, 0.3794])
        elif score_diff == 3:
            b.lights(1, 'state', bri=255, on=True, xy=[0.3426, 0.1705])
            b.lights(4, 'state', bri=255, on=True, xy=[0.3426, 0.1705])
            print("Field goal")
        elif score_diff == 1:
            b.lights(1, 'state', bri=255, on=True, xy=[0.169, 0.1308])
            b.lights(4, 'state', bri=255, on=True, xy=[0.169, 0.1308])
            print("Extra point")
        else:
            b.lights(1, 'state', bri=255, on=True, xy=[0.3344, 0.5002])
            b.lights(4, 'state', bri=255, on=True, xy=[0.3344, 0.5002])
            print("Touchdown")
        pretty_score = "Us: " + str(sea_score) + " Them: " + str(suck_score)
        print pretty_score
        time.sleep(3)
        b.lights(1, 'state', bri=255, on=False)
        b.lights(2, 'state', bri=255, on=False)
        b.lights(3, 'state', bri=255, on=False)
        b.lights(4, 'state', bri=255, on=False)
        time.sleep(1)
        b.lights(1, 'state', bri=254, on=True, xy=[0.1637, 0.3522])
        b.lights(2, 'state', bri=254, on=True, xy=[0.169, 0.1308])
        b.lights(3, 'state', bri=254, on=True, xy=[0.1497, 0.1939])
        b.lights(4, 'state', bri=254, on=True, xy=[0.2344, 0.5274])

c = C()
year, week = nflgame.live.current_year_and_week()
b.lights(1, 'state', bri=254, on=True, xy=[0.1637, 0.3522])
b.lights(2, 'state', bri=254, on=True, xy=[0.169, 0.1308])
b.lights(3, 'state', bri=254, on=True, xy=[0.1497, 0.1939])
b.lights(4, 'state', bri=254, on=True, xy=[0.2344, 0.5274])
while game_on:
    games = nflgame.games(year, week)
    if len(games) ==0:
        games = nflgame.games(year, week-1)
    plays = nflgame.combine_plays(games)
    for p in plays:
        if p.team.encode('ascii','ignore') == 'SEA':
            if len(p.events) > 0:
                if p.desc.encode('ascii','ignore').find('Shotgun') == -1:
                    event_plays.append(p.desc.encode('ascii','ignore'))
    open('nfl_events.html', 'w').close()
    for ind,item in enumerate(event_plays[-5:]):
        f = open('nfl_events.html','a')
        f.write(str(ind+1) + ": " + item + "\n")
        f.close()
    for p in games:
       if p.nice_score().encode('ascii','ignore').find('SEA') > -1:
          stupid_var = p.nice_score().encode('ascii','ignore').split(" ")
          if stupidest_var != stupid_var:
            stupidest_var = stupid_var
            if p.is_home('SEA'):
                suck_team = p.away.encode('ascii','ignore')
                suck_score = p.score_away
                sea_score = p.score_home
            else:
                suck_team = p.home.encode('ascii','ignore')
                suck_score = p.score_home
                sea_score = p.score_away
            c.score_method(sea_score, sea_score_last, suck_score, suck_score_last)
            sea_score_last = sea_score
            suck_score_last = suck_score
            game_on = p.playing()
            if game_on == False:
                winning_team = p.winner.encode('ascii','ignore')
            current_score = p.nice_score().encode('ascii','ignore')
            f = open('nfl.html','w')
            f.write("The current score is " + current_score) # python will convert \n to os.linesep
            f.close()
    time.sleep(5)
else:
    if winning_team == 'SEA':
        ending_text = "We won! Congrats everyone! The score was " + current_score
        b.lights(1, 'state', bri=254, on=False)
        b.lights(2, 'state', bri=254, on=False)
        b.lights(3, 'state', bri=254, on=False)
        b.lights(4, 'state', bri=254, on=False)
        b.lights(1, 'state', bri=254, on=True, xy=[0.1637, 0.3522])
        b.lights(2, 'state', bri=254, on=True, xy=[0.169, 0.1308])
        b.lights(3, 'state', bri=254, on=True, xy=[0.1497, 0.1939])
        b.lights(4, 'state', bri=254, on=True, xy=[0.2344, 0.5274])
        b.lights(1, 'state', bri=254, on=False)
        b.lights(2, 'state', bri=254, on=False)
        b.lights(3, 'state', bri=254, on=False)
        b.lights(4, 'state', bri=254, on=False)
        b.lights(1, 'state', bri=254, on=True, xy=[0.1637, 0.3522])
        b.lights(2, 'state', bri=254, on=True, xy=[0.169, 0.1308])
        b.lights(3, 'state', bri=254, on=True, xy=[0.1497, 0.1939])
        b.lights(4, 'state', bri=254, on=True, xy=[0.2344, 0.5274])
        b.lights(1, 'state', bri=254, on=False)
        b.lights(2, 'state', bri=254, on=False)
        b.lights(3, 'state', bri=254, on=False)
        b.lights(4, 'state', bri=254, on=False)
        b.lights(1, 'state', bri=254, on=True, xy=[0.1637, 0.3522])
        b.lights(2, 'state', bri=254, on=True, xy=[0.169, 0.1308])
        b.lights(3, 'state', bri=254, on=True, xy=[0.1497, 0.1939])
        b.lights(4, 'state', bri=254, on=True, xy=[0.2344, 0.5274])
        b.lights(1, 'state', bri=254, on=False)
        b.lights(2, 'state', bri=254, on=False)
        b.lights(3, 'state', bri=254, on=False)
        b.lights(4, 'state', bri=254, on=False)
        b.lights(1, 'state', bri=254, on=True, xy=[0.1637, 0.3522])
        b.lights(2, 'state', bri=254, on=True, xy=[0.169, 0.1308])
        b.lights(3, 'state', bri=254, on=True, xy=[0.1497, 0.1939])
        b.lights(4, 'state', bri=254, on=True, xy=[0.2344, 0.5274])
    else:
        ending_text = "We will get them next time! " + current_score
        b.lights(1, 'state', bri=254, on=False)
        b.lights(2, 'state', bri=254, on=False)
        b.lights(3, 'state', bri=254, on=False)
        b.lights(4, 'state', bri=254, on=False)
        b.lights(1, 'state', bri=255, on=True, xy=[0.6065, 0.3095])
        b.lights(2, 'state', bri=255, on=True, xy=[0.6883, 0.306])
        b.lights(3, 'state', bri=255, on=True, xy=[0.6883, 0.306])
        b.lights(4, 'state', bri=255, on=True, xy=[0.6065, 0.3095])
        b.lights(1, 'state', bri=254, on=False)
        b.lights(2, 'state', bri=254, on=False)
        b.lights(3, 'state', bri=254, on=False)
        b.lights(4, 'state', bri=254, on=False)
        b.lights(1, 'state', bri=255, on=True, xy=[0.6065, 0.3095])
        b.lights(2, 'state', bri=255, on=True, xy=[0.6883, 0.306])
        b.lights(3, 'state', bri=255, on=True, xy=[0.6883, 0.306])
        b.lights(4, 'state', bri=255, on=True, xy=[0.6065, 0.3095])
        b.lights(1, 'state', bri=254, on=False)
        b.lights(2, 'state', bri=254, on=False)
        b.lights(3, 'state', bri=254, on=False)
        b.lights(4, 'state', bri=254, on=False)
        b.lights(1, 'state', bri=255, on=True, xy=[0.6065, 0.3095])
        b.lights(2, 'state', bri=255, on=True, xy=[0.6883, 0.306])
        b.lights(3, 'state', bri=255, on=True, xy=[0.6883, 0.306])
        b.lights(4, 'state', bri=255, on=True, xy=[0.6065, 0.3095])
        b.lights(1, 'state', bri=254, on=False)
        b.lights(2, 'state', bri=254, on=False)
        b.lights(3, 'state', bri=254, on=False)
        b.lights(4, 'state', bri=254, on=False)
        b.lights(1, 'state', bri=255, on=True, xy=[0.6065, 0.3095])
        b.lights(2, 'state', bri=255, on=True, xy=[0.6883, 0.306])
        b.lights(3, 'state', bri=255, on=True, xy=[0.6883, 0.306])
        b.lights(4, 'state', bri=255, on=True, xy=[0.6065, 0.3095])
    print(ending_text)
f = open('nfl.html','w')
f.write(ending_text + "\n")
f.close()
