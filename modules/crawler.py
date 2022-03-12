import requests
from bs4 import BeautifulSoup

class Crawler:

    def info(bookID):
        url = f'https://www.esjzone.cc/detail/{bookID}.html'
        header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.36', 'cookie': 'hidden=value; _ga=GA1.2.1289323171.1643116990; ws_rr=b7a38c0453pCc7wfqg7aIkF5PYRmCBnQkO57kYuju-7IJOg_NhQTUmzT1U; ws_wt=0; ws_mem_view_bg=mycolor-6; ws_mem_view_t=mytext-0; _gid=GA1.2.1962627263.1646822663; hidden=value; msg_alert=10; ws_last_visit_code=941784efeeAk3-UeSz04cMkyCAWoYnWuHdsQ-sY465axPcsB5tFn9BrKUTwYtFXIEQa_9oC5RRAGWrKFkxbWfZ-kw; ws_last_visit_post=21fd466e04BrsH9ruN9Q2a4KKJQjWqUrEfYqmcrXa_s9ZMA-z0OgBLGLyeUpcAGQ; __cf_bm=zmtCuZ32RNYEX_jwLhmfQTrX4bmfG81VKZxxkGoEJOY-1646918670-0-AadFX1j+8jaYyZShLEd/9mM2EbOWVlFYxDU5eQmEOiW3G53UhnlAnprYuRVD6Zx/sYYpL2voF7ue+9Dc3EtmDkcw4iFqRXZ4Dj2UmEFWHc7zRV9Vgbnay00ebXYqEzLQTA==; ws_key=ebc0c6e64bUxr3b5FWOfAFOEQKPzNlJS1EJIXwEB661NJ37HRBad7fkVn55oWudek; ws_token=dd6455cde5Cdb_TS348JurUQohdCPfJF3uIZj2h5SGiExHb6x0lRc2kI8NJ7q4-w24yygIYwcmx2OAqT93uADhi50ntQ'}
        htmlFile = requests.get(url, headers=header)
        soup = BeautifulSoup(htmlFile.text, 'html.parser')
        chapterList = soup.find("div", attrs={'id':'chapterList'})
        chapters = chapterList.find_all("a")
        lastestChapter = chapters[-1]
        lastestChapterID = lastestChapter['href'][30+len(str(bookID)):-5]
        lastestChapterTitle = lastestChapter.find('p').get_text()
        bookTitle = soup.find(class_="p-t-10").get_text()      
        return lastestChapterID, lastestChapterTitle, bookTitle