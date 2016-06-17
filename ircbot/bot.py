import random
import socket
import ssl
import time

import livescore
import grandslam
import h2h

server = "chat.freenode.net"
port = 6697
channel = "#reddit-tennis"
botnick = "boxbot"
password = ""

irc_C = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc = ssl.wrap_socket(irc_C)

print ("Establishing connection to [%s]" % (server))
irc.connect((server, port))
irc.setblocking(False)
irc.send("PASS %s\n" % (password))
irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :cm201-rules\n")
irc.send("NICK "+ botnick +"\n")
irc.send("PRIVMSG nickserv :identify %s %s\r\n" % (botnick, password))
irc.send("JOIN "+ channel +"\n")

for i in range(200):
    try:
        text=irc.recv(2040)
        print (text)
    except Exception:
        continue
    time.sleep(1)

while True:
    time.sleep(2)

    try:
        text=irc.recv(2040)
        print (text)
        
        if text.find('PING') != -1:
            irc.send('PONG ' + text.split() [1] + '\r\n')

        if text.find(':.paes') != -1:
            ran = random.randint(0,5)
            if ran == 1:
                irc.send('PRIVMSG '+ channel +' :https://i.imgur.com/jpI7fDR.jpg \r\n')
            if ran == 2:
                irc.send('PRIVMSG '+ channel +' :https://i.imgur.com/p9zCyyW.jpg \r\n')
            if ran == 3:
                irc.send('PRIVMSG '+ channel +' :https://i.imgur.com/g4NB3Si.jpg \r\n')
            if ran == 4:
                irc.send('PRIVMSG '+ channel +' :https://i.imgur.com/2U3ZPAj.jpg \r\n')
            if ran == 5:
                irc.send('PRIVMSG '+ channel +' :https://i.imgur.com/nJ4Xnrs.jpg \r\n')

        if text.find(':.tommy') != -1:
            irc.send('PRIVMSG '+ channel +' :https://i.imgur.com/FtoNeTD.jpg \r\n')

        if text.find(':.gs') != -1:
            t = text.split(':.gs ')
            print t
            t = t[1]
            t = t.split()
            
            year = t[0]
            slam = t[1]

            result = grandslam.gsRes(year, slam.lower())
            print result
            irc.send('PRIVMSG '+ channel +' :'+result+' \r\n')

        if text.find(':.score') != -1:
            t = text.split(':.score ')
            t = t[1]
            t = t.split()
            
            if len(t) > 1:
                t = t[0] + ' ' + t[1]
            else:
                t = t[0]
            
            if len(t)>1:
                results = livescore.scoreSearch(t)
                result = ''
                for i in results:
                    result = result + '{' + i + '} '
                irc.send('PRIVMSG '+ channel +' :'+result+' \r\n')

        if text.find(':.h2h1'):
            t = text.split(':.h2h1 ')
            t = t[1]
            t = t.strip()
            t = t.split('/')
            p1 = t[0]
            p2 = t[1]
            if ( p1.find(' ') ):
                p1 = p1.replace(" ", "+")
                print p1

            if ( p2.find(' ') ):
                p2 = p2.replace(" ", "+")
                print p2
            result = h2h.head2head(p1, p2, 2)
            irc.send('PRIVMSG '+ channel +' :'+result+' \r\n')

        if text.find(':.h2h2'):
            t = text.split(':.h2h2 ')
            t = t[1]
            t = t.strip()
            t = t.split('/')
            p1 = t[0]
            p2 = t[1]
            if ( p1.find(' ') ):
                p1 = p1.replace(" ", "+")
                print p1

            if ( p2.find(' ') ):
                p2 = p2.replace(" ", "+")
                print p2
            result = h2h.head2head(p1, p2, 4)
            irc.send('PRIVMSG '+ channel +' :'+result+' \r\n')
            
    except Exception:
        continue
