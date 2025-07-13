from flask import Flask , render_template , request , url_for , redirect , flash
from validate import RegistrationForm

app = Flask(__name__)
app.secret_key = "secretkey"

@app.route("/" , methods = ["POST" , "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        flash(f" Welcome {name} , You registered Successfully" , "success")
        return redirect(url_for("success"))
    
    return render_template("register.html" , form = form)


@app.route("/success")
def success():
    return render_template("success.html")



if __name__ == "__main__":
    app.run(debug=True)
