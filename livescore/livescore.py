import webpage
import lxml.html as lh
import result

def scoreSearch(lookingFor):
    print 'searchin for: ' + lookingFor

    doc = webpage.scrape()
    #getting max number of tennis tournaments playing today

    maxTableCount = doc.xpath('count(//*[@id="fs"]/div/table)')+1
    maxTableCount = int(maxTableCount)

    #magic list for storing results
    results = []

    def alternate():
        while True:
            yield 5
            yield 2
            yield 0

    def findPlayer(i, j, k):
        playerTemp = doc.xpath('//*[@id="fs"]/div/table['+str(i)+']/tbody/tr['+str(j)+']/td['+str(k)+']/span/text()')
        playerTemp = playerTemp[0]
        return playerTemp
    
    for table in range(1, maxTableCount):
        maxRowCount = doc.xpath('count(//*[@id="fs"]/div/table['+str(table)+']/tbody/tr)')+1
        maxRowCount = int(maxRowCount)
        alternator = alternate()
        for row in range(1, maxRowCount):
            alt = alternator.next()
            if alt != 0:
                playerSearch = findPlayer(table, row, alt)
                if lookingFor.lower() in playerSearch.lower():
                    print 'Found player...' + playerSearch
                    if alt == 5:
                        alt = 1
                        player1 = playerSearch
                        player2 = findPlayer(table, row+1, 2)
                    if alt == 2:
                        alt = 2 #lol
                        player1 = findPlayer(table, row-1, 5)
                        player2 = playerSearch
                    results.append(result.getResult(doc, player1, player2, table, row, alt))
    return results
                    
            
            
	
