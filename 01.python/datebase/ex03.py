import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

name = input('검색학 이름: ')
query = f"SELECT addr FROM tblAddr WHERE name='{name}'"
cursor.execute(query)

record = cursor.fetchone()
print(type(record), record)

if record:
    print(f"{name}은 {record[0]}에 살고 있습니다.")
else:
    print(f"{name}은 없는 이름입니다.")

cursor.close()
con.close()
