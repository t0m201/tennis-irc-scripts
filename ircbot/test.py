import livescore
import grandslam
import h2h

text = ':.h2h1 fede/murra'
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
print h2h.head2head(p1, p2, 2)
