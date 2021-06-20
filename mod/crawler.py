import requests
from bs4 import BeautifulSoup

class crawler:
    def info(books):
        id = []
        title = []
        length = len(books["Id"])
        for i in range(len(books["Id"])):
            url = f"https://www.esjzone.cc/detail/{ books['Id'][i] }.html"
            htmlFile = requests.get(url)
            soup = BeautifulSoup(htmlFile.text, 'lxml')
            link = soup.find(id="integration").find_all('a') #在文章區塊尋找所有連結
            id.append(link[-1]["href"][30+len(books["Id"][i]):-5]) # 文章id
            title.append(soup.find(class_="p-t-10").get_text())
        return id, title, length
        