import sqlite3
import pandas
conn = sqlite3.connect('movies.db') 
conn.cursor()

conn.execute('CREATE TABLE IF NOT EXISTS MoviesINFO(Movie VARCHAR,LeadActor TEXT,ReleaseYear INT,Director TEXT)')
print('Table created inside db')

conn.commit()
conn.close()