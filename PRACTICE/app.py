from flask import Flask  , Response , redirect ,request , url_for , render_template , session , flash

app = Flask(__name__)
app.secret_key = "secretkey"

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/submit" , methods = ["POST"])
def submit():
    name = request.form.get("username")
    password = request.form.get("password")

    if not name :
        flash("Name cannot be empty") 
        return redirect(url_for("login"))

    if name == "pratham" and password == "pass":
        return render_template("thank.html" , name = name )
    else:
       flash("Invalid credentials")
       return redirect(url_for("login"))
    
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
