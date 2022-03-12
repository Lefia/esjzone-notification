import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent

url = f'https://www.kadokado.com.tw/book/10?tab=catalog'
user_agent = generate_user_agent()
header = {'user-agent': user_agent,}
htmlFile = requests.get(url, headers=header)
soup = BeautifulSoup(htmlFile.text, 'html.parser')
print(soup)