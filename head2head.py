import requests
from pprint import pprint
from lxml import html

#expected command with two search tokens separated by /

#rq = ".h2hm fed/mur"
rq = ".h2hw wil/sha"

#checking if searching for atp or wta
if rq.find('.h2hm') !=-1:
    gender = 2
if rq.find('.h2hw') !=-1:
    gender = 4
if gender == 2:
    rq = rq.split('.h2hm')
if gender == 4:
    rq = rq.split('.h2hw')
if (gender == 1 or 2):
    rq = rq[1]
    rq = rq.strip()
    rq = rq.split('/')
    p1 = rq[0]
    p2 = rq[1]
    if ( p1.find(' ') ):
        p1 = p1.replace(" ", "+")
        print p1

    if ( p2.find(' ') ):
        p2 = p2.replace(" ", "+")
        print p2

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
    print p1name
    print p2name

    score = tree.xpath('//td[@class="gScore"]/text()')
    print score
    score = ''.join(score)
    print score

    h2h = p1name + ' ' + score + ' ' + p2name
    print h2h
    #irc.send('PRIVMSG '+ channel +' : ' + h2h +'\r\n')
    gender = 0

