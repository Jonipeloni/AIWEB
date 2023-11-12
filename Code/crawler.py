from queue import Queue
from typing import Set, Any

import requests
from bs4 import BeautifulSoup

from whoosh.index import create_in
from whoosh.fields import *

import indexing

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

# Create an index in the directory indexdir (the directory must already exist!)
ix = indexing.get_index()
writer = ix.writer()


# Algorithm:
# Initialize Cue with start URL
q = Queue()
url = "https://vm009.rz.uos.de/crawl/"


q.put(url + "index.html")

# inititalize variable
current_url = 0
history: set[Any] = set()
next_entry = 0
end = 0
print("hello")

# While stack is not empty:
while 0 == q.empty() or end < 10:
    end = + 1
    current_url = q.get()
    history.add(current_url)
    r = requests.get(current_url)

    # was wenn status code 404 ist was bedeuted das?
    print(r.status_code)
    print(r.headers)

    # extracting url content and write it into the index
    soup = BeautifulSoup(r.content, 'html.parser')
    title = str(soup.title.string)
    writer.add_document(title=title,url=current_url, content=soup.text)
    writer.commit()

    for l in soup.find_all("a"):
        href = l['href']
        next_entry = url + href
        if next_entry not in history:
            q.put(next_entry)

print(history)





# If not visited recently:
# Get the content
# Analyse it and updates the index
# Analyse it, find links to other websites and add links to stack (push)
# Update visited lst
