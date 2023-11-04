from queue import Queue
import requests
from bs4 import BeautifulSoup

"""
r = requests.get('https://www.joice-hamburg.de')
print(r.status_code)
print(r.headers)
#print(r.content)

soup = BeautifulSoup(r.content, 'html.parser')
print(soup.title.text)
for l in soup.find_all("a"):
    print(l['href'])
    
    
r = requests.get('https://vm009.rz.uos.de/')
"""









# Algorithm:
# Initialize Cue with start URL
q = Queue()
url = "https://vm009.rz.uos.de/crawl/"

q.put(url + "index.html")

# inititalize variable
current_url = 0
history = []
next_entry = 0
end = 0
print("hello")

# While stack is not empty:
while 0 == q.empty() or end < 10:
    end = + 1
    current_url = q.get()
    history.append(current_url)
    r = requests.get(current_url)
    print(r.status_code)
    print(r.headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    for l in soup.find_all("a"):
        href = l['href']
        next_entry = url + href
        if next_entry not in history:
            q.put(next_entry)


print(history[:])





# If not visited recently:
# Get the content
# Analyse it and updates the index
# Analyse it, find links to other websites and add links to stack (push)
# Update visited lst
