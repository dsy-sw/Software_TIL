import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute("DELETE FROM tblAddr WHERE name='κΉμν'")
con.commit()

cursor.close()
con.close()
