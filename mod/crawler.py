import requests
from bs4 import BeautifulSoup

class Crawler:

    def info(book):
        url = f"https://www.esjzone.cc/detail/{ book }.html"
        htmlFile = requests.get(url, headers=headers)
        soup = BeautifulSoup(htmlFile.text, 'lxml')
        link = soup.find(id="integration").find_all('a')
        a = link[-1]
        lastest = a['href'][30+len(book):-5]
        title = a.find('p').get_text()
        book_title = soup.find(class_="p-t-10").get_text()
        return lastest, book_title, title
        