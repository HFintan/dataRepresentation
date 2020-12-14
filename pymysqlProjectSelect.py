import mysql.connector
import dbconfig as cfg

db = mysql.connector.connect (
    host=cfg.mysql['host'],
    user=cfg.mysql['user'],
    password=cfg.mysql['password'],
    database=cfg.mysql['database']
)

cursor = db.cursor()
sql = "select * from student where id = %s"
values = (1,)

cursor.execute(sql,values)
result = cursor.fetchall()
for x in result:
    print(x)
