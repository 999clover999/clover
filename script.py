import requests
from bs4 import BeautifulSoup
import random
import urllib.request



def catalogSpider():
    print("\n")
    print("--- IT DOESN'T MATTER WHICH ONE YOU INPUT FOR NOW (05/01/2019) THIS INPUT IS THERE TO CATCH ANY ERRORS IN FUTURE ---\n")
    
    whichBoard = input("Please enter which board 4Chan or 4Channel: ")
    boardVar = input('Please enter a name of board with / /: ')
    ID = input('Please enter thred ID: ')
    if whichBoard == "4Chan":
        finalUrl = 'https://boards.4chan.org' + str(boardVar)
    else:
        finalUrl = 'https://boards.4channel.org' + str(boardVar)
    url = str(finalUrl) + 'thread/' + str(ID)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'html.parser')
    for link in soup.findAll('a', {'class': 'fileThumb'}):
        href = 'https:' + link.get('href')
        imageName = href[-10:]
        print (href)
        print(imageName) #Debug stuff, also so you know it's doing something
        name = random.randrange(1, 1000000)
        full_name = str(name) + imageName
        print (full_name)
        urllib.request.urlretrieve(href, full_name)


                               
while True:
 catalogSpider()
