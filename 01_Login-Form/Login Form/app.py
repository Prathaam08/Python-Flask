from flask import Flask , request ,session , redirect , url_for , Response

app = Flask(__name__)
app.secret_key = "supersecret"

@app.route("/" , methods = ["POST" ,"GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid credentials!! , Try again" , mimetype = "text/plain")
    
    return '''
            <h2>Login Page </h2>
            <form method = "POST">
            Username : <input type = "text" name = "username"><br>
            Password : <input type = "text" name = "password"><br>
            <input type = "submit" value = "Login" >
            </form>
'''

@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
        <h2>Welcome , {session["user"]}!!</h2>
        <a href = {url_for('logout')}> Logout </a>
    '''
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user" , None)
    return redirect(url_for("login"))