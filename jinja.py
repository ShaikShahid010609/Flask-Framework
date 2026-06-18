# Building url dynamically using jinja template in flask
#variable rule 
# -->{{}} expression to print the value of a variable in html page
# -->{{%   %}}conditional statements and loops in html page
# -->{{# #}} this is used to write comments in html page
from flask import Flask, render_template, request,redirect, url_for
app = Flask(__name__)

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        # email = request.form.get("email") --- IGNORE ---
        return f"Hello, {name}! Welcome to Flask!"
    return render_template("form.html")

@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    return render_template("result.html", results=res)

@app.route("/submit", methods=["GET","POST"])
def submit():
    if request.method == "POST":
        science = int(request.form.get("science"))
        maths = int(request.form.get("maths"))
        english = int(request.form.get("english"))
        datascience = int(request.form.get("datascience"))

        total = science + maths + english + datascience
        average = total / 4

        return redirect(url_for("success", score=average))

if __name__ == '__main__':
    app.run(debug=True)