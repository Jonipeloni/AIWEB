from flask import Flask
import whoosh

#define global variable
app = Flask(__name__)
#wenn dieser path abgerufen wird, wird die folgende funktion gecalled
@app.route("/")
def start():
    return "Hello world"


from whoosh.qparser import QueryParser

with ix.searcher() as searcher:
    # find entries with the words 'first' AND 'last'
    query = QueryParser("content", ix.schema).parse("first last")
    results = searcher.search(query)

    # print all results
    for r in results:
        print(r)



