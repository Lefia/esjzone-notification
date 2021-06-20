from mod.file import Data, Content
from mod.crawler import crawler

data = Data("./books.json")
Books = data.open()

content = Content("")

lastest, title, length = crawler.info(Books)

for i in range(length): 
    
    if Books["Lastest"][i] != lastest[i]: #如果文章更新了

        content.add(lastest[i], title[i])
        Books["Lastest"][i] = lastest[i] #更新最新小說id

content.exists()

data.close(Books)