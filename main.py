from flask import Flask, render_template, request, redirect, session
import db

# Create our web host
app = Flask(__name__)
app.secret_key = "gtg"

@app.route("/")
def home():
    data = db.GetAll()
    return render_template("index.html", guesses=data)

@app.route("/add", methods=("GET", "POST"))
def add():

    if request.method == "POST":
        date = request.form["date"]
        score = request.form["score"]
        game = request.form["game"]
        guesser = request.form["guesser"]

        db.AddGuess(date, score, game, guesser)

        return redirect("/")

    return render_template("add.html")


@app.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if db.Login(username, password):
            session['username'] = username
            return redirect("/")

    return render_template("login.html")

@app.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        db.RegisterUser(username, password)

        return redirect("/login")

    return render_template("register.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

app.run(debug=True, port=5000)