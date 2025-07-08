from flask import Flask , render_template , request , url_for , redirect

app = Flask(__name__)


@app.route("/")
def home():
    return redirect(url_for("feedback"))

@app.route("/feedback" , methods = ["POST" ,"GET"])
def feedback():
    if request.method == "POST":
        name = request.form.get("username")
        message = request.form.get("message")

        return render_template("thankyou.html" , user = name , message = message)  
    
    return render_template("feedback.html")


if __name__ == "__main__":
    app.run(debug=True)
