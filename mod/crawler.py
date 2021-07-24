import requests
from bs4 import BeautifulSoup

class Crawler:

    def info(book, wantBookTitle=False):
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'}
        url = f"https://www.esjzone.cc/detail/{ book }.html"
        htmlFile = requests.get(url, headers=headers)
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
        