import nflgame
import time
import sys

suck_team = ""
stupidest_var=""
sea_score = 0
sea_score_last = 0
suck_score = 0
suck_score_last = 0
game_on = True

class C:
    def score_method(self, sea_score, sea_score_last, suck_score, suck_score_last):
    	print [sea_score, sea_score_last, suck_score, suck_score_last]
    	cheer_time = True
    	if int(sea_score) != int(sea_score_last):
        	score_diff = int(sea_score) - int(sea_score_last)
    	else:
    		cheer_time = False
    		score_diff = int(suck_score) - int(suck_score_last)
    	if score_diff == 2:
    		print("safety or two point conversion")
    		if cheer_time:
    			print("good stuff")
    		else:
    			print(" bad stuff")
    	elif score_diff == 3:
    		print(" field goal")
    		if cheer_time:
    			print("good stuff")
    		else:
    			print(" bad stuff")
    	elif score_diff == 1:
    		print("extra point")
    		if cheer_time:
    			print("good stuff")
    		else:
    			print(" bad stuff")
    	else:
    		print("touchdown or starting")
    		if cheer_time:
    			print("good stuff")
    		else:
    			print(" bad stuff")

c = C()
year, week = nflgame.live.current_year_and_week()
while game_on:
    games = nflgame.games(year, week)
    for p in games:
       if p.nice_score().encode('ascii','ignore').find('SEA') > -1:
          stupid_var = p.nice_score().encode('ascii','ignore').split(" ")
          if stupidest_var == stupid_var:
            print(p)
          elif stupidest_var != stupid_var:
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
    time.sleep(5)
else:
	winner = p.winner.encode('ascii','ignore')
	print("Game is over!")
	if winner == 'SEA':
		print("we did it congrats everyone!")
	else:
		print("we will get them next time!")