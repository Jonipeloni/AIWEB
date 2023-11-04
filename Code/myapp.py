from flask import Flask
import whoosh

#define global variable
app = Flask(__name__)
#wenn dieser path abgerufen wird, wird die folgende funktion gecalled
@app.route("/")
def start():
    return "Hello world"



