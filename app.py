from flask import Flask, render_template, request, session

app = Flask(__name__)
@app.route("/"):
def login():
    username = request.form["username"]
    password = request.form["password"]
    if(username == "poo" and password == "pee"):
        session["username"] = username
        return redirect("/woo")
    else:
        return "You entered the wrong information!"
    return render_template("form.html")

@app.route("/woo"):
def logged():
    return render_template("greet.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
