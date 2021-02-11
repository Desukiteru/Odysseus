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

class bufor_package:
     def __init__(self, domen, keys):
          self.pack = []
          self.fetch(domen, keys)

     def fetch(self, domen, keys):
          file = BeautifulSoup(str(requests.get(str(domen)).text),"html.parser")
          buf = ((file.find(attrs=keys[0])).find_all(keys[1]))
          bufor = []
          i= 0
          for zle in buf:
               try:
                    tyt = zle.find(keys[2]).text
                    price = zle.find(attrs=keys[3]).get_text()
                    desc = zle.find(attrs=keys[4]).get_text()
                    tags = zle.find(attrs=keys[5]).get_text()
                    link = zle.find(keys[6]).get(keys[7])
               except:
                    pass
                    bufor.append([])
                    bufor[i].append(tyt)
                    bufor[i].append(price)
                    bufor[i].append(desc)
                    bufor[i].append(tags)
                    bufor[i].append(link)
                    i=i+1
          listm = []
          [listm.append(a) for a in bufor if a not in listm]
          self.pack = listm

class ofert:
     def __init__(self, buf):
          self.title= ""
          self.price = ""
          self.desc = ""
          self.tags = ""
          self.link = ""
          self.fetch(buf)
     def fetch(self, buf):
          self.title = buf[0]
          self.price = buf[1]
          self.desc = buf[2]
          self.tags = buf[3]
          self.link= buf[4]
     def iam(self):
          print(self.title)
          print(self.price)
          print(self.desc)
          print(self.tags)
          print(self.link)

class baza:
     def __init__(self):
          self.base = []


keys=[{"id":"job-list"},["div", "wrapper"],"h2",
      {"class":"price"},{"class": "description"},{"class": "tags"},["a", "href"],"href"]
a= bufor_package("https://useme.com/pl/jobs/category/strony-internetowe,1/",keys).pack
ab = []
for ofer in a:
     ab.append(ofert(ofer))

for ofer in ab:
     ofer.iam()

