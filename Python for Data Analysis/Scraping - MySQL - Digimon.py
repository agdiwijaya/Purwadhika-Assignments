from bs4 import BeautifulSoup
import requests
import mysql.connector


############ SCRAPPING THE WEBSITE ###########

# Extracting Page
url = 'http://digidb.io/digimon-list/'
web = requests.get(url)
out = BeautifulSoup(web.content, 'html.parser')

# Extracting Data (without image link)

data = []
for i in out.find_all('td'):
    data.append(i.text.strip())

# Extracting Image Link
link = []
for i in out.find_all('img'):
    link.append(i['src'])
img = link[2:343]

# Creating Dataset
datadigimon = []
count = list(range(0,len(data),13))
for j in range(341):
    i = count[j]
    tupledigimon = f"({data[i]}, '{data[i+1]}', '{img[j]}', '{data[i+2]}', '{data[i+3]}', '{data[i+4]}', {data[i+5]}, {data[i+6]}, {data[i+7]}, {data[i+8]}, {data[i+9]}, {data[i+10]}, {data[i+11]}, {data[i+12]})"
    datadigimon.append(tupledigimon)

########### CREATING SQL TABLE ###########

# Connecting to MySQL
myDB = {
    'user': 'root',
    'password': 'agdees11',
    'host': 'localhost',
    'port' : 3307}
conn = mysql.connector.connect(**myDB)
cr = conn.cursor()

# #Drop Database
# cr.execute("DROP DATABASE datadigimon")

# Creating Database
cr.execute("CREATE DATABASE datadigimon")
cr.execute("USE datadigimon")

# Creating table
querytable = """CREATE TABLE list_digimon (No SMALLINT, Nama CHAR(30), Image_Link CHAR(50), 
Stage CHAR(20), Type CHAR(20), Attribute CHAR(20), Memory SMALLINT, EquipSlot SMALLINT, 
HP SMALLINT, SP SMALLINT, Attack SMALLINT, Defense SMALLINT, Intelligence SMALLINT, Speed SMALLINT)"""
cr.execute(querytable)
conn.commit()

# Data Entry
for i in datadigimon:
    querydata = f"INSERT INTO list_digimon VALUES {i}"
    cr.execute(querydata)
    conn.commit()