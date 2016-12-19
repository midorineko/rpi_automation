import nflgame

games = nflgame.games(2016, week=13)
players = nflgame.combine_game_stats(games)
for p in players.rushing().sort('rushing_yds').limit(5):
    msg = '%s %d carries for %d yards and %d TDs'
    print msg % (p, p.rushing_att, p.rushing_yds, p.rushing_tds)



import nflgame

games = nflgame.games(2016, week=13)
plays = nflgame.combine_plays(games)
for p in plays.sort('passing_yds'):
    print p


import nflgame
import time
woot = ""
b=[]
tush=[]
year, week = nflgame.live.current_year_and_week()
while True:
games = nflgame.games(year, week)
for p in games:
if p.nice_score().encode('ascii','ignore').find('SEA') > -1:
woot = p.nice_score()
b = woot.split(" ")
tush.push(b[woot.split(" ").index('SEA')+1])
print p
time.sleep(10)


    .limit(5)


    nice_score


import nflgame

year, week = nflgame.live.current_year_and_week()
games = nflgame.games(year, week)
games[0].nice_score()

import nflgame
import time

x=1
year, week = nflgame.live.current_year_and_week()
games = nflgame.games(year, week)
while x>0
for p in games:
if p.nice_score().encode('ascii','ignore').contain('SEA')
print p.nice_score().encode('ascii','ignore')
time.sleep(15)
