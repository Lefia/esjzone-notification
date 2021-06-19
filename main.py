import requests
import json 
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText 
from email.header import Header 
import os

with open("/mnt/c/Users/Lefia/Documents/Projects/esjzone/data.json", 'r') as jsonfile:
    data = json.load(jsonfile)

email = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')
content=""

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
    #email內容
    msg = MIMEText(f'<html><body>{content} <b>更新了!</b></body></html>', 'html', 'utf-8')
    msg['Subject'] = Header("Esjzone 小說更新通知", 'utf-8') 
    msg['From'] = email
    msg['To'] = "lefia1222@gmail.com"

    mySMTP = smtplib.SMTP("smtp.gmail.com", 587) #伺服器
    mySMTP.ehlo() #打招呼
    mySMTP.starttls() #加密
    mySMTP.login(email, password) #登入
    mySMTP.sendmail(email, "lefia1222@gmail.com",  msg.as_string()) #傳送

with open("/mnt/c/Users/Lefia/Documents/Projects/esjzone/data.json", "w") as jsonfile:
    json.dump(data, jsonfile)