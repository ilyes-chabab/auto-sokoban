import sqlite3

class Database:
    def __init__(self, db_name="classement.db"):  # Changed to classement.db
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS leaderboard
                               (id INTEGER PRIMARY KEY AUTOINCREMENT, time REAL)''')
        self.conn.commit()

    def insert_time(self, time):
        self.cursor.execute("INSERT INTO leaderboard (time) VALUES (?)", (time,))
        self.conn.commit()

    def get_top_times(self, limit=10):
        self.cursor.execute("SELECT time FROM leaderboard ORDER BY time ASC LIMIT ?", (limit,))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

