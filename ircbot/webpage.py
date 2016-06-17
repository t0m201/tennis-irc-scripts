import lxml.html as lh
from selenium import webdriver

def scrape():
    #open up invisible browser instance to grab page
    browser = webdriver.PhantomJS()
    browser.set_window_size(0, 0)

    #link plus grabbing
    link = 'http://www.flashscore.com/tennis/'
    browser.get(link)
    content = browser.page_source
    browser.quit()

    #tree from lxml
    doc = lh.fromstring(content)
    return doc
