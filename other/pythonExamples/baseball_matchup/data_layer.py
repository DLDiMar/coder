import sqlite3

def create_table():
    conn = sqlite3.connect('baseball.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS matchups
                 (pitcher text, batter text, outcome text)''')
    conn.commit()
    conn.close()

def store_matchup(pitcher, batter, outcome):
    conn = sqlite3.connect('baseball.db')
    c = conn.cursor()
    c.execute("INSERT INTO matchups VALUES (?, ?, ?)", (pitcher, batter, outcome))
    conn.commit()
    conn.close()

def get_previous_matchup(pitcher, batter):
    conn = sqlite3.connect('baseball.db')
    c = conn.cursor()
    c.execute("SELECT outcome FROM matchups WHERE pitcher=? AND batter=?", (pitcher, batter))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return 'No previous matchup'