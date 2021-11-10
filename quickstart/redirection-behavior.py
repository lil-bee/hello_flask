from flask import Flask
app = Flask(__name__)

@app.route("/")
#belakangnya ada '/'
@app.route("/projects/")
def proects():
    return "The project Page"

#belakangnya gaada '/' tar jadinya error kalo routingnya pake'/'
@app.route("/about")
def about():
    return "About Page"