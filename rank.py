import requests
from lxml import html

lookingFor = 'svitolina'
lookingFor = lookingFor.lower()

counter = 1
maxRow = 2000
found = False

page1 = requests.get('http://www.flashscore.com/tennis/rankings/atp/')
tree1 = html.fromstring(page1.text)

page2 = requests.get('http://www.flashscore.com/tennis/rankings/wta/')
tree2 = html.fromstring(page2.text)

while found == False:
    atp = True
    wta = True

    if atp:
        try:
            player1 = tree1.xpath('//*[@id="ranking-table-results_35851"]/tbody/tr['+ str(counter) +']/td[2]/a/text()')
            player1 = player1[0]
            player1 = player1.strip()
            player1Lower = player1.lower()

            rank1 = tree1.xpath('//*[@id="ranking-table-results_35851"]/tbody/tr['+ str(counter) +']/td[1]/text()')
            rank1 = rank1[0]
            
        except:
            atp = False
        
    if wta:
        try:
            player2 = tree2.xpath('//*[@id="ranking-table-results_35853"]/tbody/tr['+ str(counter) + ']/td[2]/a/text()')
            player2 = player2[0]
            player2 = player2.strip()
            player2Lower = player2.lower()

            rank2 = tree2.xpath('//*[@id="ranking-table-results_35853"]/tbody/tr['+ str(counter) +']/td[1]/text()')
            rank2 = rank2[0]
        except:
            wta = False

    if lookingFor in player1Lower:
        print rank1 + player1
        found = True

    if lookingFor in player2Lower:
        print rank2 + player2
        found = True
        
    counter = counter + 1
