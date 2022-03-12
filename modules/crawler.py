import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent

class Crawler:

    def info(bookID):
        url = f'https://www.esjzone.cc/detail/{bookID}.html'
        user_agent = generate_user_agent()
        header = {
            'user-agent': user_agent,
            'cookie': 'hidden=value; _ga=GA1.2.1289323171.1643116990; ws_rr=b7a38c0453pCc7wfqg7aIkF5PYRmCBnQkO57kYuju-7IJOg_NhQTUmzT1U; ws_wt=0; ws_mem_view_bg=mycolor-6; hidden=value; msg_alert=10; _gid=GA1.2.1427312831.1647056801; ws_mem_view_t=mytext-1; ws_last_uid=b251f0a71eMIAu0vz9kuZxaecrRKBHtzCVLYXOZ3ZJAL6jjw; ws_last_code=2dd8ba868bbLF0IBeCIBM5-T_lDUmCLKJVeVz8uAXTk-osOWtVD_Ea5eBLMw; ws_last_visit_post=cdca54b939_3F74O5JQj5QsQZymiRMBdoAnO2mV-KT5CubEZnCuJtl44T2lssSD7bQ21Hs-2i8j9nIBcygWwtE0jYUGIeUE8QrifkcBJdYa060; _gat=1; __cf_bm=s7co9SpWV3dxli7pdK0suERBOAgTJlD3JWHvuD6t1GY-1647081010-0-AbStOYfCJDTHaRRY14i2mWGp7hc85Vg/cIZxDZHE4y3xe6fCmIBaJrg6m3CqVQs0rmywl1MS9oit5zSi69DoPA7qKiXpqg68LUp6ESedXGp/wAoDi9SdpXFcrNT+9UMgdw==; ws_key=f83a6b16a765Ks42SAMa7uWubbqZV2nTBKKGUe_ITWzkLpHtC7dd16OYoy; ws_token=604c146fedQujXQrR1DB1dRecUPSe-QO0mlKyQDVxzsxTz8y_UjM2k0vyq8RcZUGGBGZjhqZlNiCcYImjRpOOmWEcjqQ; ws_last_visit_code=d0e548b9afqDn7UZGOm9FeOWbfbA9ts9y2xkCNspbFMT6ldegEShblG6MspKMI63QzRuJNbfnoGYlX_Qu4Ix2j8ThYW6J1RN2kPAvfaA'
        }
        htmlFile = requests.get(url, headers=header)
        soup = BeautifulSoup(htmlFile.text, 'html.parser')
        chapterList = soup.find("div", attrs={'id':'chapterList'})
        chapters = chapterList.find_all("a")
        lastestChapter = chapters[-1]
        lastestChapterID = lastestChapter['href'][30+len(str(bookID)):-5]
        lastestChapterTitle = lastestChapter.find('p').get_text()
        bookTitle = soup.find(class_="p-t-10").get_text()      
        return lastestChapterID, lastestChapterTitle, bookTitle