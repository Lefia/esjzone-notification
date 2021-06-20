from mod.file import Data, Content
from mod.crawler import Crawler

data = Data("./books.json")
Books = data.open()

content = Content("")

for i in range(len(Books["Id"])): 
    lastest, book_title, title = Crawler.info(Books["Id"][i])
    if Books["Lastest"][i] != lastest: #如果文章更新了
        content.add(Books["Id"][i], lastest, book_title, title)
        Books["Lastest"][i] = lastest #更新最新小說id

content.exists()

data.close(Books)