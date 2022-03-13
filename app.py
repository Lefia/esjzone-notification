from pydoc import stripid
from modules.crawler import Crawler
from opencc import OpenCC
import sqlite3

cc = OpenCC('s2t')

while(True):
    data = sqlite3.connect('books.sqlite')
    cur = data.cursor()
    cmd = input('請輸入指令：(1) List (2) Add  (3) Remove (4) Clear\n>> ')

    if cmd == "list":
        print("-"*10)
        cur.execute('SELECT * FROM books')
        books = cur.fetchall()
        for row in books:
            bookID = row[0]
            bookTitle = row[2]
            print(f'{bookTitle} {bookID}')

    elif cmd == "add":
        print("-"*10)
        bookID = input("請輸入小說網址\n>> ")
        bookID = bookID[30:-5]
        lastestChapterID, lastestChapterTitle, bookTitle = Crawler.info(bookID)
        lastestChapterTitle = cc.convert(lastestChapterTitle)
        bookTitle = cc.convert(bookTitle) 
        bookTitle = stripid(bookTitle)
        cur.execute(F'INSERT INTO books VALUES({bookID}, {lastestChapterID}, \'{bookTitle}\')')
        data.commit()
        cur.close()
        print("-"*10)
        print("書籍名稱：" + bookTitle)
        print("最新一話：" + lastestChapterTitle)
        print("成功加入收藏!")

    elif cmd == "remove":
        print("-"*10)
        bookID = input("請輸入小說ID\n>> ")
        bookID = int(bookID)
        cur.execute(f'DELETE FROM books WHERE ID = {bookID}')
        data.commit()
        cur.close()
        print("移除成功")

    elif cmd == "clear":
        break
    
    else:
        print("-"*10)
        print("指令有誤")
    
    print("-"*10)