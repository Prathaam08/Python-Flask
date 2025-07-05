from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def student_profile():
    return render_template(
        "student_profile.html",
        name = "Pratham",
        is_Topper = True,
        subjects = ["Maths" , "Science" , "History"]
    )


