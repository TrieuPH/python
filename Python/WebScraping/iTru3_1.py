import requests

url = 'https://www.vietstock.vn'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url, headers=headers)
print(result.content.decode())
# export result.content.decode() to text file
with open('iTru3_1.txt', 'w', encoding='utf-8') as f:
    f.write(result.content.decode())
# export all links to text file
from bs4 import BeautifulSoup
soup = BeautifulSoup(result.content.decode(), 'html.parser')
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
with open('iTru3_2.txt', 'w', encoding='utf-8') as f:
    for link in links:
        f.write(link.get('href') + '\n')
