import lxml.html as lh

def getResult(doc, player1, player2, table, row, alt):
    
    #function for grabbing each game number from set and plopping into list
    #i=table, j=row, k=+/- row number, m=first/second player, n=start <td> number
    def gameGrab(i, j, k, m, n):
        for num in range(n, n+5):
            game = doc.xpath('//*[@id="fs"]/div/table['+str(i)+']/tbody/tr['+str(j+k)+']/td['+str(num)+']/text()')
            
            #if found character is unicode, i.e. there is no set score, stop this loop
            if isinstance(game[0], unicode):
                break
            if m == 1:
                player1Games.append(game[0])
            if m == 2:
                player2Games.append(game[0])

    #grabs current game score
    def scoreGrab(i, j):
        tempScore = doc.xpath('//*[@id="fs"]/div/table['+str(table)+']/tbody/tr['+str(row+i)+']/td['+str(j)+']/text()')
        tempScore = tempScore[0]
        return tempScore

    #grabs time of match starting plus if match is cancelled/walkover
    def statusGrab(i):
        timeCheck = doc.xpath('//*[@id="fs"]/div/table['+str(table)+']/tbody/tr['+str(row+i)+']/td['+str(2)+']/text()')
        timeCheck = timeCheck[0]

        matchCheck = doc.xpath('//*[@id="fs"]/div/table['+str(table)+']/tbody/tr['+str(row+i)+']/td['+str(3)+']/span/text()')
        matchCheck = matchCheck[0]
        return timeCheck, matchCheck

    #returns string of games in order depending on who has won match or if match in progress
    def gameCollate(i):
        games = ''
        if i == 1:
            for num in range(0, len(player1Games)):
                games = games + str(player1Games[num]) + '-' + str(player2Games[num]) + ', '
            games = games[:-2]
        if i == 2:
            for num in range(0, len(player1Games)):
                games = games + str(player2Games[num]) + '-' + str(player1Games[num]) + ', '
            games = games[:-2]
        return games

    #computes which player is serving. i think this works
    #might not work
    def serveCheck(i):
        if i == 1:
            serve = doc.xpath('//*[@id="fs"]/div/table['+str(table)+']/tbody/tr['+str(row)+']/td['+str(4)+']/span/span')
            if len(serve) > 0:
                return 1
            serve = doc.xpath('//*[@id="fs"]/div/table['+str(table)+']/tbody/tr['+str(row+1)+']/td['+str(1)+']/span/span')
            if len(serve) > 0:
                return 2
        if i == 2:
            serve = doc.xpath('//*[@id="fs"]/div/table['+str(table)+']/tbody/tr['+str(row-1)+']/td['+str(1)+']/span/span')
            if len(serve) > 0:
                return 2
            serve = doc.xpath('//*[@id="fs"]/div/table['+str(table)+']/tbody/tr['+str(row)+']/td['+str(4)+']/span/span')
            if len(serve) > 0:
                return 1
        
    #lists for storing games form each set
    player1Games = []
    player1Score = 0
    player2Games = []
    player2Score = 0
    
    #build score string
    if alt == 1:
        gameGrab(table, row, 0, 1, 7)
        gameGrab(table, row, 1, 2, 4)
        player1Score = scoreGrab(0, 12)
        player2Score = scoreGrab(1, 9)
        matchTime, matchStatus = statusGrab(0)
            
    if alt == 2:
        gameGrab(table, row, -1, 1, 7)
        gameGrab(table, row, 0, 2, 4)
        player1Score = scoreGrab(-1, 12)
        player2Score = scoreGrab(0, 9)
        matchTime, matchStatus = statusGrab(-1)

    result = player1 + ' vs ' + player2 + ': '

    #checking match status
    if matchStatus == 'Walkover':
        result = result + matchStatus
    if matchStatus == 'FRO':
        result = result + 'Final result only!'
    if matchStatus == 'Cancelled':
        result = result + matchStatus

    #basically if the match hasn't started yet
    if matchStatus != 'Walkover' and matchStatus != 'FRO' and matchStatus != 'Cancelled' and len(player1Games) == 0:
        result = result + 'are playing today at '+ matchTime +' BST!'
    elif len(player1Games) > 0:
        #check which player won and layout string in correct order
        if matchStatus == 'Finished':
            player1Games = map(int, player1Games)
            player2Games = map(int, player2Games)
            if sum(player1Games) > sum(player2Games):
                result = player1 + ' d. ' + player2 + ': ' + gameCollate(1)
            else:
                result = player2 + ' d. ' + player1 + ': ' + gameCollate(2)
        #match in progress
        else:
            if serveCheck(alt) == 1:
                result = result + gameCollate(1) + ' [*' + player1Score + ' - ' + player2Score + ']'
            if serveCheck(alt) == 2:
                result = result + gameCollate(1) + ' [' + player1Score + ' - *' + player2Score + ']'
    return result

