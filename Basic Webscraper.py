import requests
from bs4 import BeautifulSoup

Request=requests.get("http://pythonhow.com/example.html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
Content=Request.content

#print(Content)
#print(type(Content))


Soup=BeautifulSoup(Content,'html.parser')
#print(Soup.prettify())


#print(type(Soup))

all=Soup.find_all("div",{"class":"cities"})
#print(all)

#print(all[0])

#print(all[0].find_all("h2")[0].text)

for cities in all:
    print(cities.find_all("h2")[0].text)

"""

for i in range(len(all)):
    print(all[i].find_all("h2")[0].text)

"""










