import requests
import json 
from bs4 import BeautifulSoup
import os

with open("./data.json", 'r') as jsonfile:
    data = json.load(jsonfile)

f = open('content.html','w')
content = ""

for i in range(5): #

    url = "https://www.esjzone.cc/detail/" + data["Books"][i] + ".html"
    htmlFile = requests.get(url)

    soup = BeautifulSoup(htmlFile.text, 'lxml')
    link = soup.find(id="integration").find_all('a') #在文章區塊尋找所有連結
    id = link[-1]["href"][30+len(data["Books"][i]):-5] #取文章id

    title = soup.find(class_="p-t-10").get_text()

    if id != data["Lastest"][i]: #如果文章更新了

        content += '<a href="https://esjzone.cc/forum/' + data["Books"][i] + "/" + id + '.html">' + title + '</a><br>'
        
        data["Lastest"][i] = id #更新最新小說id

if content != "":
    f.write(f'<html><body>{content} <b>更新了!</b></body></html>')
    f.close()
    os.environ["JSON_CHANGE"] = "1"

with open("./data.json", "w") as jsonfile:
    json.dump(data, jsonfile)