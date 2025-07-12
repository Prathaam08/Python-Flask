from flask import Flask , render_template , request , url_for , redirect , flash

app = Flask(__name__)
app.secret_key = "my-secret-key"


@app.route("/" ,  methods = ["POST" ,"GET"])
def form():

    if request.method == "POST":
        name = request.form.get("username")
        if not name:
            flash("Name cannot be empty")
            return redirect(url_for("form"))
        flash(f"Thanks {name}, Your Feedback is sent")
        return redirect(url_for("thankyou"))
    return render_template("form.html")
   

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")


if __name__ == "__main__":
    app.run(debug=True)

