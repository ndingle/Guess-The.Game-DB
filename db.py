import sqlite3

def GetDB():
    db = sqlite3.connect(".database/datasource.db")
    db.row_factory = sqlite3.Row
    return db

def GetAll():
    db = GetDB()

    # Query the db
    data = db.execute("SELECT * FROM guesses ORDER BY date DESC").fetchall()
    return data

def Add(date, score, game, guesser):
    db = GetDB()

    # Add the new score to the DB
    db.execute("INSERT INTO guesses (date, score, game, guesser) VALUES (?, ?, ?, ?)", 
               (date, score, game, guesser))
    db.commit()