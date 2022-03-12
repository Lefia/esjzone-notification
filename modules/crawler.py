import requests
from bs4 import BeautifulSoup

class Crawler:

    def info(bookID):
        url = f'https://www.esjzone.cc/detail/{bookID}.html'
        header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.36', 'cookie': 'hidden=value; _ga=GA1.2.1289323171.1643116990; ws_rr=b7a38c0453pCc7wfqg7aIkF5PYRmCBnQkO57kYuju-7IJOg_NhQTUmzT1U; ws_wt=0; ws_mem_view_bg=mycolor-6; hidden=value; msg_alert=10; _gid=GA1.2.1427312831.1647056801; ws_last_visit_code=20382fabd6iCyFnnyeHm6zi8YYjro_rXsfnmtUswaC2cMb9Fscs1JcV3ijTKZGJ9Kn1Qfc8Ke4; ws_mem_view_t=mytext-1; ws_last_visit_post=49f02cb8b6rctXl5N_vGI_VBNTsPzbjJkw7mwiwmHEiHjWSjx3DrHaUUqGu9SzRaC-63HUv7Q; ws_key=b42a211f98trq6m0_C0CrPiestCy6wTYxe-hiRFDSzkrWEl0yzoLQITb9Otz2yST90; ws_token=63cf958469-fvcByt147eQq8Lj4KjFcuXaRlkeMO3cPd8Z03wEZSqFqrjy4Fp58thYZIRWsQVvuPn5Yv_gMRYkipKcpw'}
        htmlFile = requests.get(url, headers=header)
        soup = BeautifulSoup(htmlFile.text, 'html.parser')
        chapterList = soup.find("div", attrs={'id':'chapterList'})
        chapters = chapterList.find_all("a")
        lastestChapter = chapters[-1]
        lastestChapterID = lastestChapter['href'][30+len(str(bookID)):-5]
        lastestChapterTitle = lastestChapter.find('p').get_text()
        bookTitle = soup.find(class_="p-t-10").get_text()      
        return lastestChapterID, lastestChapterTitle, bookTitle