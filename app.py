from mod.file import Data, Content
from mod.crawler import Crawler
from opencc import OpenCC

cc = OpenCC('s2t')
data = Data("./books.json")

while(True):
    Books = data.open()
    cmd = input("請輸入指令：")

    if cmd == "list":
        for i in range(len(Books["BookTitle"])):
            print(Books["BookTitle"][i] + " " + Books["Id"][i])

    elif cmd == "add":
        print("-"*10)
        BookId = input("請輸入小說網址\n>> ")
        BookId = BookId[30:-5]
        lastest, title, BookTitle = Crawler.info(BookId, True)
        title = cc.convert(title)
        BookTitle = cc.convert(BookTitle) 
        Books["BookTitle"].append(BookTitle) 
        Books["Id"].append(BookId) 
        Books["Lastest"].append(lastest) 
        print("-"*10)
        print("書籍名稱：" + BookTitle)
        print("最新一話：" + title)
        print("成功加入收藏!")

    elif cmd == "remove":
        print("-"*10)
        BookId = input("請輸入小說ID\n>> ")
        for i in range(len(Books["Id"])):
            if Books["Id"][i] == BookId:
                print("書籍名稱：" + Books["BookTitle"][i])
                del Books["Id"][i]
                del Books["Lastest"][i]
                del Books["BookTitle"][i]
                print("從收藏中移除")
                break

    elif cmd == "quit":
        print("-"*10)
        break
    
    else:
        print("-"*10)
        print("指令有誤")
    
    print("-"*10)
    

    data.close(Books)