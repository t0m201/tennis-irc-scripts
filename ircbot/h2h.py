import requests
from pprint import pprint
from lxml import html

#expected command with two search tokens separated by /

#rq = ".h2hm fed/mur"
#rq = ".h2hw wil/sha"

def head2head(p1, p2, gender):
        #scraping from tennisexplorer.com
        page = requests.get('http://www.tennisexplorer.com/list-players/?search-text-pl='+p1)
        tree = html.fromstring(page.text)

        p1link = tree.xpath('//tbody[@class="flags"]/tr[1]/td['+str(gender)+']/a/@href')
        p1link = ''.join(p1link)
        p1link = p1link.strip('/')
        p1link = p1link.split('/')
        p1link = p1link[1]
        print p1link

        page = requests.get('http://www.tennisexplorer.com/list-players/?search-text-pl='+p2)
        tree = html.fromstring(page.text)

        p2link = tree.xpath('//tbody[@class="flags"]/tr[1]/td['+str(gender)+']/a/@href')
        p2link = ''.join(p2link)
        p2link = p2link.strip('/')
        p2link = p2link.split('/')
        p2link = p2link[1]
        print p2link

        page = requests.get('http://www.tennisexplorer.com/mutual/' + p1link +'/' + p2link +'/')
        tree = html.fromstring(page.text)

        #building string
        pNames = tree.xpath('//th[@class="plName"]/a/text()')
        p1name = pNames[0]
        p2name = pNames[1]
        
        p1name = p1name.split()
        p1name = p1name[1] + ' ' + p1name[0]
        
        p2name = p2name.split()
        p2name = p2name[1] + ' ' + p2name[0]

        score = tree.xpath('//td[@class="gScore"]/text()')
        score = ''.join(score)

        h2h = p1name + ' ' + score + ' ' + p2name
        print h2h

        surfaceList = [0, 0, 0, 0, 0]
        rowCount = tree.xpath('count(//*[@id="center"]/div[2]/div/div/table/tbody/tr)')+1
        rowCount = int(rowCount)
        for row in range(1, rowCount):
            if row % 2 != 0:
                surface = tree.xpath('//*[@id="center"]/div[2]/div/div/table/tbody/tr['+str(row)+']/td[5]/span//@title')
                if len(surface) > 0:
                    surface = surface[0]
                    if surface == 'Clay':
                        surfaceList[0] = surfaceList[0] + 1
                    if surface == 'Grass':
                        surfaceList[1] = surfaceList[1] + 1
                    if surface == 'Hard':
                        surfaceList[2] = surfaceList[2] + 1
                    if surface == 'Indoors':
                        surfaceList[3] = surfaceList[3] + 1
                else:
                    surfaceList[4] = surfaceList[4] + 1

        if sum(surfaceList) > 1:
            h2h = h2h + ': '
            for num in range(0, 5):
                if surfaceList[num] != 0:
                    surface = (float(surfaceList[num])/float(sum(surfaceList)))*100
                    surface = round(surface, 2)
                    print surface
                    if num == 0:
                        h2h = h2h + str(surface) + '% Clay, '
                    if num == 1:
                        h2h = h2h + str(surface) + '% Grass, '
                    if num == 2:
                        h2h = h2h + str(surface) + '% Hard, '
                    if num == 3:
                        h2h = h2h + str(surface) + '% Indoors, '
                    if num == 4:
                        h2h = h2h + str(surface) + '% Unknown surface, '
            h2h = h2h[:-2]
        return h2h
