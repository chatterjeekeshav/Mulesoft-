import sqlite3
c= sqlite3.connect('Movies.db')
print(c) 
c.cursor()

c.execute("INSERT INTO MoviesINFO VALUES('Endgame ','Tony stark        ','2020','Marval')")
c.execute("INSERT INTO MoviesINFO VALUES('ABCD    ','PrabhuDeva       ','2018','Karan johar')")

c.commit()
c.close()