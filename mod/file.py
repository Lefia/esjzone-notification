import json 
import os

class Data:
    def __init__(self, data_location):
        self.data_location = data_location
    
    def open(self):
        with open(self.data_location, 'r') as jsonfile:
            return json.load(jsonfile)
    
    def close(self, data):
        with open(self.data_location, "w") as jsonfile:
            json.dump(data, jsonfile)

class Content:
    def __init__(self, text):
        self.text = text
    
    def add(self, id, lastest, book_title, title):
        self.text += f'<p>{ book_title }</p><br><a href="https://esjzone.cc/forum/{ id }/{ lastest }.html">{ title }</a><br>'
    
    def exists(self):
        if self.text != "":
            f = open('content.html','w')
            f.write(f'<html><body>{ self.text }<b>更新了!</b></body></html>')
            f.close()
        else:
            if os.path.exists("content.html"):
                os.remove("content.html")
            else:
                pass