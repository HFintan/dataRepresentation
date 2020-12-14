import mysql.connector
import re
import dbconfig as cfg

mydb = mysql.connector.connect(
    host=cfg.mysql['host'],
    user=cfg.mysql['username'],
    password=cfg.mysql['password'],
    database=cfg.mysql['database']
)

while True:
    value = input('PPSN:')
    try:
        value = str(value

cursor = db.cursor()
sql = "insert into vaccine (PPSN,name,age,LEA,occupation,stage,vaccinated) values (%s,%s,%s,%s,%s,%s,%s)"
values = ("Mary","21")

cursor.execute(sql,values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)
