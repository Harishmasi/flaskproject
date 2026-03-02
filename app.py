from flask import Flask, url_for, redirect, render_template

app = Flask(__name__)

@app.route("/")
def room():
    return render_template("index.html")

@app.route("/<name>")
def call(name):
    return f"Hello {name}"

@app.route("/app")
def route():
    return redirect(url_for("db"))

@app.route("/db")
def db():
    return "This is the Database"

if __name__ == "__main__" :
    app.run()