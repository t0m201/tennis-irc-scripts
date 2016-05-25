# tennis-irc-scripts
collection of python scripts that grab cool tennis stats from webpages primarily designed for irc

grandslam.py -
  returns the results of a grandslam specified year. expected command would be ".gs year slam" where year is the year and slam is the slam. for example, ".gs 2002 f" would return the results for the 2002 french open
  
head2head.py -
  returns the head to head stats of two tennis players. expected command would be either ".h2hw player/player" or ".h2hm player/player" for wta/atp respectively. doesnt need to take full names but needs the / separater. example: ".h2hm fed/mur" would return the head to head for federer and murray
  
rank.py -
  simple script that loops through two web pages trying to match a string for a player name and it returns the players full name + their rank
