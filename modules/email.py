import os

class Email:
    def __init__(self, text):
        self.text = text
    
    def add(self, bookID, lastestChapterID, bookTitle, lastestChapterTitle):
        self.text += f'<h2>{ bookTitle }</h2><a href="https://esjzone.cc/forum/{ bookID }/{ lastestChapterID }.html">{ lastestChapterTitle }</a><br>'
    
    def fileExists(self):
        if self.text != '':
            f = open('email.html','w')
            f.write(f'<html><body>{ self.text }</body></html>')
            f.close()
        else:
            if os.path.exists("email.html"):
                os.remove("email.html")