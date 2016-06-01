# tennis-irc-scripts
collection of python scripts that grab cool tennis stats from webpages primarily designed for irc, they all primarily use lxml

grandslam.py -
  returns the results of a grandslam specified year. expected command would be ".gs year slam" where year is the year and slam is the slam. for example, ".gs 2002 f" would return the results for the 2002 french open
  
head2head.py -
  returns the head to head stats of two tennis players. expected command would be either ".h2hw player/player" or ".h2hm player/player" for wta/atp respectively. doesnt need to take full names but needs the / separater. example: ".h2hm fed/mur" would return the head to head for federer and murray

livescore.py -
  needs phantomjs and selenium installed. currently, the script is basically a linear search through html tables, returning matching players. ".score murr" would return the current scoreline for any player that has "murr" in their name. the main function is called "scoreSearch" located in livescore.py which contains the loop. the code has been fragmented as such due a stupid amount of silly functions. webpage.py simply returns a scraped webpage and result.py formats the string and grabs the score and other silly stuff like that
