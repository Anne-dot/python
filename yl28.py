#https://medium.com/@nishantsahoo/which-movie-should-i-watch-5c83a3c0f5b1

#Loe läbi artikkel.
#Kas suudad mõista ja selgitada, mis on Web Scraping?
#Millised on selle tegevuse eetilisuse ja viisakuse reeglid?
#Tee ise artiklis kirjeldatud projekt läbi ja kirjuta programm.
#Kohanda programmi Kuressaare Ametikooli tunniplaanist info kätte saamiseks.

import urllib

from bs3 import BeautifulSoup
url = "enter_url_here"
ourUrl = urllib3.PoolManager().request('GET', url).data
soup = BeautifulSoup(ourUrl, "lxml")
print(soup.find('title').text)