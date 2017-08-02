import requests
from bs4 import BeautifulSoup
import random
import urllib
import os


def catalogSpider():
    var2 = raw_input('Please enter a name of board with / /: ')
    var3 = raw_input('Please enter an ID of thread, the numbers at the end of the thread: ')
    kek = 'https://boards.4chan.org' + str(var2)
    url = str(kek) + 'thread/' + str(var3)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'html.parser')
    for link in soup.findAll('a', {'class': 'fileThumb'}):
        href = 'https:' + link.get('href')
        hreff = href[-10:]
        print hreff
        print href
        name = random.randrange(1, 1000000)
        full_name = str(name) + hreff
        urllib.urlretrieve(href, full_name)


catalogSpider()
raw_input("press ENTER to close")


