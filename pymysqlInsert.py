import mysql.connector

db = mysql.connector.connect (
    host="localhost",
    user="fintan",
    password="password",
    database="datarepresentation"
)

cursor = db.cursor()
sql = "insert into student (name,age) values (%s,%s)"
values = ("Mary","21")

cursor.execute(sql,values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)