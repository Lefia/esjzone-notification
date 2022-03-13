from pydoc import stripid
import sqlite3
from time import sleep
from modules.crawler import Crawler
from modules.email import Email

data = sqlite3.connect('books.sqlite')
cur = data.cursor()

cur.execute('SELECT * FROM books')
books = cur.fetchall()

email = Email('')

for row in books:
    bookID = row[0]
    savedChapterID = str(row[1])
    lastestChapterID, lastestChapterTitle, bookTitle = Crawler.info(bookID)
    lastestChapterTitle = stripid(lastestChapterTitle)
    if savedChapterID != lastestChapterID: 
        email.add(bookID, lastestChapterID, bookTitle, lastestChapterTitle)
        cur.execute(f'UPDATE books SET Lastest = {lastestChapterID} WHERE ID = {bookID}')
    sleep(3)

email.fileExists()

data.commit()
data.close()
    
    


# cur.execute("INSERT INTO books VALUES(1619378930, 138753, '龍鎖的奧日 - 心中的“芯”')")
# conn.commit()