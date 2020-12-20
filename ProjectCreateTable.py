import mysql.connector
import dbconfig as cfg

db = mysql.connector.connect(
    host=cfg.mysql['host'],
    user=cfg.mysql['user'],
    password=cfg.mysql['password'],
    database=cfg.mysql['database']
)

cursor = db.cursor()

# Breaking lines should be neater and nicer, but threw an error; maybe come back FH
sql="CREATE TABLE people (PPSN INT PRIMARY KEY, name VARCHAR(63) NOT NULL,  email VARCHAR(63) NOT NULL, age INT, location VARCHAR(255), medical BOOLEAN, occupation VARCHAR(63), stage INT, vaccinated_1 BOOLEAN, vaccinated_2 BOOLEAN);"

cursor.execute(sql)
