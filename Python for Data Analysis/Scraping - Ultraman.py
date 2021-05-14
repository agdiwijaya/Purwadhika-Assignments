from bs4 import BeautifulSoup
import requests
import json
url = 'https://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/'
web = requests.get(url)
out = BeautifulSoup(web.content, 'html.parser')


karakter = []
for i in out.find_all('strong'):
    karakter.append(i.text)

ultraman = karakter[2:36]
monster = karakter[37:110]

# print(ultraman)
# print(monster)

keyultra = []
valueultra = []
for x in ultraman:
    keyultra.append(x[:2])
    valueultra.append(x[3:])

# for i in range(0, len(keyultra)): 
#     keyultra[i] = int(keyultra[i]) 
ultramania = dict(zip(keyultra, valueultra))

# print(ultramania)


keymonster = []
valuemonster = []
for y in monster:
    keymonster.append(y[:2])
    valuemonster.append(y[3:])

# for i in range(0, len(keymonster)): 
#     keymonster[i] = int(keymonster[i]) 
monsterkaiju = dict(zip(keymonster, valuemonster))

# print(monsterkaiju)


scrap = [dict(zip(['Ultraman','Monsters'],[ultramania, monsterkaiju]))]
with open('scrappingultraman.json', 'w') as file:
    json.dump(scrap, file)
print("File Created")

# print(scrap)