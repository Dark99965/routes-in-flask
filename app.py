# imports

from flask import Flask
from flask import render_template

# main app

app = Flask(__name__)

@app.route("/")
def home(): 
    return render_template("home.html")

@app.route("/<someurl>")
def notfound(someurl):
    return render_template("404.html", url=someurl)