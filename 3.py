import sqlite3

con = sqlite3.connect('Movies.db')
cur = con.cursor()


cursor = cur.execute("SELECT * FROM MoviesINFO")
print('\n')
print(cur.fetchall())

cur.execute("SELECT * From MoviesINFO where ReleaseYear=2018")
print('\n')
print(cur.fetchall())

cur.execute("SELECT Movie,LeadActor From MoviesINFO ")
print(cur.fetchall())

con.commit()
con.close()