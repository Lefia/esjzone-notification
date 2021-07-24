import requests
from bs4 import BeautifulSoup

class Crawler:

    def info(book, wantBookTitle=False):
        url = f"https://www.esjzone.cc/detail/{ book }.html"
        htmlFile = requests.get(url)
        soup = BeautifulSoup(htmlFile.text, 'lxml')
        chapterlist = soup.find("div", attrs={"id":"chapterList"})
        link_div = chapterlist.find_all("a")
        link = link_div[-1]
        lastest = link['href'][30+len(book):-5]
        title = link.find('p').get_text()
        print(title)

        if wantBookTitle == True:
            bookTitle = soup.find(class_="p-t-10").get_text()
            return lastest, title, bookTitle
        else :
            return lastest, title
        