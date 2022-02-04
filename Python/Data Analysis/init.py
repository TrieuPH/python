### USING CONFIG FILE INI
import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {}
config['DEFAULT']['host'] = 'localhost'
config['DEFAULT']['port'] = '27017'
config['DEFAULT']['dataExport'] = 'D:\\DataExport\\'
with open('config.ini','w') as configfile:
    config.write(configfile)

### ANOTHER EXAMPLE USING xml instead of ini
'''
from bs4 import BeautifulSoup

with open("config.xml") as f:
    content = f.read()

y = BeautifulSoup(content, features="lxml")
print(y.mysql.host.contents[0])
for tag in y.other.preprocessing_queue.li:
    print(tag)
'''