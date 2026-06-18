from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        # email = request.form.get("email") --- IGNORE ---
        return f"Hello, {name}! Welcome to Flask!"
    return render_template("form.html")

if __name__ == '__main__':
    app.run(debug=True)
