from flask import Flask ,render_template , url_for ,request

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/submit" , methods = ["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")

    # if username == "pratham" and password == "pass":
    #     return render_template("welcome.html" , name = username)


    # For Multiple users
    valid_user =  {
        'admin' : 'pass',
        'pratham' : '123',
        'shawn' : 'ss12'
    }

    if username in valid_user and password == valid_user[username]:
        return render_template("welcome.html" , name = username)
    else:
        return "Invalid credentials!!"
    
@app.route("/welcome")
def welcome():
    return render_template("welcome.html")