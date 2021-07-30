from mod.file import Data, Content
from mod.crawler import Crawler
from time import sleep

data = Data("./books.json")
Books = data.open()

content = Content("")

for i in range(len(Books["Id"])): 
    lastest, title = Crawler.info(Books["Id"][i])
    if Books["Lastest"][i] != lastest: 
        content.add(Books["Id"][i], lastest, Books["BookTitle"][i], title)
        Books["Lastest"][i] = lastest
    sleep(3) 

content.exists()

data.close(Books)