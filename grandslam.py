from lxml import html
import requests

#expect command format, year followed by either a/f/w/u for grand slam
#text = '.gs 2014 f'

def gsRes(year, slam):
    #creating correct url name for scraping
    if slam == 'w':
        slam = 'Wimbledon_Championships'
    if slam == 'u':
        slam = 'US_Open'
        if 1968 > int(year):
            slam = "U.S._National_Championships"
    if slam == 'f':
        slam = 'French_Open'
        if 1968 > int(year):
            slam = "French_Championships"
            print slam
    if slam == 'a':
        slam = 'Australian_Open'
        if 1968 > int(year):
            slam = "Australian_Championships"
      
    title = year + ' ' + slam + ' Results: '

    #scraping from wikipedia
    wikiLinkM = 'http://en.wikipedia.org/wiki/' + year + '_' + slam + '_%E2%80%93_Men%27s_Singles'
    wikiLinkW = 'http://en.wikipedia.org/wiki/' + year + '_' + slam + '_%E2%80%93_Women%27s_Singles'

    def scrape(link):
      page = requests.get(link)
      tree = html.fromstring(page.content)

      champ = tree.xpath('//div[@id="bodyContent"]/div[4]/table/tr[3]/td[1]/a/text()')
      champ = champ[0]
      champ = champ.encode('utf-8')

      loser = tree.xpath('//div[@id="bodyContent"]/div[4]/table/tr[4]/td[1]/a/text()')
      loser = loser[0]
      loser = loser.encode('utf-8')
      score = tree.xpath('//div[@id="bodyContent"]/div[4]/table/tr[5]/td[1]/text()')

      score = [w.encode('utf-8') for w in score]
      score = ''.join(score)
      score = score.replace("\xe2\x80\x93", "-")
      score = score.replace(",", "")
      scoreLine = champ + ' d. ' + loser + ' ' + score
      return scoreLine

    mens = scrape(wikiLinkM)
    womens = scrape(wikiLinkW)

    result = title + womens + ', ' + mens
    return result
