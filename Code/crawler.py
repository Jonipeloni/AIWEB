import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.joice-hamburg.de')
print(r.status_code)
print(r.headers)
#print(r.content)

soup = BeautifulSoup(r.content, 'html.parser')
print(soup.title.text)
for l in soup.find_all("a"):
    print(l['href'])
    
    
r = requests.get('https://vm009.rz.uos.de/')
