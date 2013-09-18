import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE proverbia
    (id integer primary key, proverbio text unique)
''')

conn.commit()
conn.close()