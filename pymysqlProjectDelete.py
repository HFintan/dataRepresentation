import mysql.connector
import dbconfig as cfg

mydb = mysql.connector.connect(
    host=cfg.mysql['host'],
    user=cfg.mysql['user'],
    password=cfg.mysql['password'],
    database=cfg.mysql['database']
)


cursor = mydb.cursor()
sql = "delete from vaccine where ppsn = %s"
values = (1,)

cursor.execute(sql,values)

mydb.commit()
print("delete done")
