from mod.file import Data, Content
from mod.crawler import crawler

data = Data("./Books.json")
Books = data.open()



data.close(Books)