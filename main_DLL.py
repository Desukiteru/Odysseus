import configparser
from bs4 import BeautifulSoup
import requests

class config:
     def __init__(self):
          self.base_channel = 0
          self.token = ""
          self.fetch()

     def fetch(self):
          config = configparser.ConfigParser()
          config.read('config.ini')
          self.token = config['Main']['token']
          self.base_channel = config['Main']['base_channel']


class buforPackage:
     def __init__(self, dane):
          self.site = dane[0]
          self.keys = dane[1]
          self.main = dane[2]
          self.fetchall(self.main)

     def handlerBS(self, a, b):
          x = BeautifulSoup(str(a.select(b)), "html.parser")
          return x

     def fetchall(self, main):
          keys = self.keys
          file = BeautifulSoup(str(requests.get(self.site).text), "html.parser")
          buf = (file.find(**main)).children
          ab = []
          for a in buf:
               if a != "\n":
                    ab.append(a)

          zle = []
          i = 0
          for ofert in ab:
               if i <= 5 and (self.handlerBS(ofert, keys[0]).text != "[]"):
                    zle.append([])
                    zle[i].append(self.handlerBS(ofert, keys[0]).text)  # t
                    zle[i].append(self.handlerBS(ofert, keys[1]).text)  # p
                    zle[i].append(self.handlerBS(ofert, keys[2]).text)  # d
                    zle[i].append(self.handlerBS(ofert, keys[3]).text)  # t
                    zle[i].append(ofert.find(keys[4])['href'])  # l
                    i = i + 1

          self.pack = zle


class base:
     def __init__(self):
          self.seed = []
          self.basse = []

     def addseed(self, site, keys, main):
          self.seed.append([site, keys, main])

     def refresh(self):
          self.basse = []
          for site in self.seed:
               bufor = buforPackage(site)
               self.basse.append([site[0], bufor])


somtin = base()
somtin.addseed('https://oferia.pl/zlecenia/programowanie-it', ['h2', '.price', '.listing-order-content', '--//--', 'a'],
               {'class': 'l-listing-maincol'})
somtin.refresh()
site = somtin.basse[0][1].pack[0]
print(site)
