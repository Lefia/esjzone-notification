import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent



class Crawler:

    def info(bookID):
        url = f'https://www.esjzone.cc/detail/{bookID}.html'
        user_agent = generate_user_agent()
        header = {'user-agent': user_agent, 'cookie': 'ws_token=d1522bcc8dqBMmK4gdguYxYJf0aIZsFb5YzLKDGRYGlWygcbdF9vDgwhy2Tc5VcTcS0CdIyB_ODZt-L00aHEjY9HDlpQ;ws_key=5d1cb43c14Q_ZTeDlAEYvjvkASjctD42D6AgjLKTjGJ4bP2-uW9cDhYUpbu2xfjDk8vA;ws_rr=b7a38c0453pCc7wfqg7aIkF5PYRmCBnQkO57kYuju-7IJOg_NhQTUmzT1U;ws_wt=0'}
        htmlFile = requests.get(url, headers=header)
        soup = BeautifulSoup(htmlFile.text, 'html.parser')
        chapterList = soup.find("div", attrs={'id':'chapterList'})
        chapters = chapterList.find_all("a")
        lastestChapter = chapters[-1]
        lastestChapterID = lastestChapter['href'][30+len(str(bookID)):-5]
        lastestChapterTitle = lastestChapter.find('p').get_text()
        bookTitle = soup.find(class_="p-t-10").get_text()      
        return lastestChapterID, lastestChapterTitle, bookTitle