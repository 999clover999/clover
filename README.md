import requests


from bs4 import BeautifulSoup


import random


import urllib


import sys




def catalogSpider1():
    
    var2 = raw_input('Please enter a name of board with / /: ')
    
    var3 = raw_input('Please enter an ID of thread, the numbers at the end of the thread: ')
   
    kek = 'https://boards.4chan.org' + str(var2)
    
    url = str(kek) + 'thread/' + str(var3)
    
    source_code = requests.get(url)
    
    plain_text = source_code.text
    
    soup = BeautifulSoup(plain_text, "html.parser")
   
    for link in soup.findAll('a', {'class': 'fileThumb'}):
        
        href = 'https:' + link.get('href')
       
        name = random.randrange(1, 1000)
        
        full_name = str(name) + '.jpg'
        
        urllib.urlretrieve(href, full_name)


def catalogSpider2():
    
    var2 = raw_input('Please enter a name of board with / /: ')
    
    var3 = raw_input('Please enter an ID of thread, the numbers at the end of the thread: ')
    
    kek = 'https://boards.4chan.org' + str(var2)
    
    url = str(kek) + 'thread/' + str(var3)
    
    source_code = requests.get(url)
    
    plain_text = source_code.text
    
    soup = BeautifulSoup(plain_text, "html.parser")
    
    for link in soup.findAll('a', {'class': 'fileThumb'}):
        
        href = 'https:' + link.get('href')
        
        name = random.randrange(1, 1000)
        
        full_name = str(name) + '.png'
        
        urllib.urlretrieve(href, full_name)

def catalogSpider3():
        
        var2 = raw_input('Please enter a name of board with / /: ')
        
        var3 = raw_input('Please enter an ID of thread, the numbers at the end of the thread: ')
        
        kek = 'https://boards.4chan.org' + str(var2)
        
        url = str(kek) + 'thread/' + str(var3)
        
        source_code = requests.get(url)
        
        plain_text = source_code.text
        
        soup = BeautifulSoup(plain_text, "html.parser")
        
        for link in soup.findAll('a', {'class': 'fileThumb'}):
            
            href = 'https:' + link.get('href')
            
            name = random.randrange(1, 1000)
            
            full_name = str(name) + '.gif'
            
            urllib.urlretrieve(href, full_name)


def catalogSpider4():
    
    var2 = raw_input('Please enter a name of board with / /: ')
    
    var3 = raw_input('Please enter an ID of thread, the numbers at the end of the thread: ')
    
    kek = 'https://boards.4chan.org' + str(var2)
    
    url = str(kek) + 'thread/' + str(var3)
    
    source_code = requests.get(url)
    
    plain_text = source_code.text
    
    soup = BeautifulSoup(plain_text, "html.parser")
    
    for link in soup.findAll('a', {'class': 'fileThumb'}):
        
        href = 'https:' + link.get('href')
        
        name = random.randrange(1, 1000)
        
        full_name = str(name) + '.webm'
        
        urllib.urlretrieve(href, full_name)






var1 = raw_input('Which one are we working with ? gif, jpg, webm or png ?: ')


if var1 == 'jpg':
    
    catalogSpider1()

elif var1 == 'png':
    
    catalogSpider2()

elif var1 == 'gif':
    
    catalogSpider3()

elif var1 == 'webm':
    
    catalogSpider4()

else:sys.exit()



print 'You should move the hentai you just got to another folder.'


raw_input("press ENTER to close")


