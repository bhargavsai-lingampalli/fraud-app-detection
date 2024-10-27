import sqlite3


con = sqlite3.connect('apps.db')
cur = con.cursor()

cur.execute('delete from app;')
con.commit()