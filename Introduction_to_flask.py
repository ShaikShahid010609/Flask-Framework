from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "WELCOME TO FLASK"
@app.route("/home")
def home():
    return "WELCOME TO HOME"

if __name__ == '__main__':
    app.run(debug = True)