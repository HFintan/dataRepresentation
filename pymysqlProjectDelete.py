import mysql.connector
import dbconfig as cfg

mydb = mysql.connector.connect(
    host=cfg.mysql['host'],
    user=cfg.mysql['username'],
    password=cfg.mysql['password'],
    database=cfg.mysql['database']
)

cursor = db.cursor()
sql = "delete from vaccine where PPS no. = %s"
values = (1,)

cursor.execute(sql,values)

db.commit()
print("Deleted.")
