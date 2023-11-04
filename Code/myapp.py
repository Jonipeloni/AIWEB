from flask import Flask
#define global variable
app = Flask(__name__)
#wenn dieser path abgerufen wird, wird die folgende funktion gecalled
@app.route("/")
def start():
    return "Hello world"
