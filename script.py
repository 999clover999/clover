import requests
from bs4 import BeautifulSoup
import random
import urllib
import os


def catalogSpider():
    var2 = raw_input('Please enter a name of board with / /: ')
    var3 = raw_input('Please enter thred ID: ')
    kek = 'https://boards.4chan.org' + str(var2)
    url = str(kek) + 'thread/' + str(var3)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'html.parser')
    for link in soup.findAll('a', {'class': 'fileThumb'}):
        href = 'https:' + link.get('href')
        hreff = href[-10:]
        print href                            #Debug stuff, also so you know it's doing something
        name = random.randrange(1, 1000000)
        full_name = str(name) + hreff
        print full_name
        urllib.urlretrieve(href, full_name)


topkek = True                                   #while True is enough
while topkek == True:
 catalogSpider()


