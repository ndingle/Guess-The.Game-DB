from flask import Flask, render_template, request, redirect
import db

# Create our web host
app = Flask(__name__)

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

        db.Add(date, score, game, guesser)

        return redirect("/")

    return render_template("add.html")

app.run(debug=True, port=5000)