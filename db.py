import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash


def GetDB():
    db = sqlite3.connect(".database/datasource.db")
    db.row_factory = sqlite3.Row
    return db


def GetAll():
    db = GetDB()

    # Query the db
    data = db.execute("SELECT * FROM guesses ORDER BY date DESC").fetchall()
    return data


def AddGuess(date, score, game, guesser):
    db = GetDB()

    # Add the new score to the DB
    db.execute("INSERT INTO guesses (date, score, game, guesser) VALUES (?, ?, ?, ?)", 
               (date, score, game, guesser))
    db.commit()


def RegisterUser(username, password):
    db = GetDB()

    # Add the new user to the DB
    try:
        db.execute("INSERT INTO users(username, password) VALUES (?, ?)",
                (username, generate_password_hash(password),))
        db.commit()
    except sqlite3.IntegrityError:
        print ("Username already exists")


def Login(username, password):
    db = GetDB()

    # Check if we have a correct username and password
    user = db.execute("SELECT * from users WHERE username = ?", (username,)).fetchone()

    if not user is None:
        if check_password_hash(user['password'], password):
            return user
    
    return None
