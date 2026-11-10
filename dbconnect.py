#sql = structured query language
import sqlite3

con = sqlite3.connect("to_do_list.db")
con.row_factory = sqlite3.Row

cur = con.cursor()
# this means that we are creating a table


cur.execute('''  CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT  NOT NULL,
            status TEXT NOT NULL DEFAULT 'Pending'
            )
            ''')


con.commit()
con.close()