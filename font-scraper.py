from bs4 import BeautifulSoup
import urllib.request as urllib2
import re
import requests
import os

#os.mkdir('data')


full_links = list()
for page in range(2, 2291):
    url = f'https://www.1001freefonts.com/new-fonts-{page}.php'
    req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
    con = urllib2.urlopen(req)
    soup = BeautifulSoup(con)
    for link in soup.findAll('a', attrs={'href': re.compile('^/d/')}):
        links = link.get('href').split()        
        for i in links:
            full_link = 'https://www.1001freefonts.com' + i
            r = requests.get(full_link, stream=True, headers={'User-agent': 'Mozilla/5.0'})
            font_link = f'{os.getcwd()}\\data{i[8:]}'
            with open(font_link, 'wb') as f:
                f.write(r.content)
            full_links.append(full_link)
    if page % 50 == 0:
        print(page)