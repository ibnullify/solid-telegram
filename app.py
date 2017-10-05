from flask import Flask, render_template, request, session, redirect
import os

app = Flask(__name__)
app.secret_key = os.urandom(26)
@app.route("/")
def login():
    username = ""
    if "username" in session:
        username = session["username"]
        return render_template("greet.html", username= username)
    return render_template("form.html", username = username)
       
@app.route("/woo", methods=["GET","POST"])
def logged():
    if "username" in session:
        session.pop("username")
    username = request.form["username"]
    password = request.form["password"]
    if(username == "poo" and password == "pee"):
        session["username"] = username
        return render_template("greet.html", username= username)
    if(username != "poo"):
        return "You did not enter correct username!!!! Go <a href='/'>back</a>"
    if(password != "pee"):
        return "You did not enter correct password!!!! Go <a href='/'>back</a>"

@app.route("/loggedout", methods=["GET","POST"])
def loggedput():
    if "username" in session:
        session.pop("username")
    return "If you were logged in, you've been logged out!!! Go <a href='/'>back</a>"

if __name__ == "__main__":
    app.debug = True
    app.run()
