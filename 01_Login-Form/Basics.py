from flask import Flask , request

app = Flask(__name__)

@app.route("/")
def homepage():
    return 'Hello user! , This is my first flask app'

@app.route("/about")
def about():
    return 'This is about page'

@app.route("/contact")
def contact():
    return 'This is a contact us page'

@app.route("/submit" , methods = ["POST" , "GET"])
def submit():
    if request.method == "POST":
        return 'You send data to server'
    else:
        return 'You are just viewing the Page'
