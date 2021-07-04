import requests
from bs4 import BeautifulSoup

class Crawler:

    def info(book, wantBookTitle=False):
        url = f"https://www.esjzone.cc/detail/{ book }.html"
        htmlFile = requests.get(url)
        soup = BeautifulSoup(htmlFile.text, 'lxml')
        link = soup.find(id="integration").find_all('a')
        a = link[-1]
        lastest = a['href'][30+len(book):-5]
        title = a.find('p').get_text()

        if wantBookTitle == True:
            bookTitle = soup.find(class_="p-t-10").get_text()
            return lastest, title, bookTitle
        else :
            return lastest, title
        