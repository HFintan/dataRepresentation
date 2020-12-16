import mysql.connector
import dbconfig as cfg

mydb = mysql.connector.connect(
    host=cfg.mysql['host'],
    user=cfg.mysql['user'],
    password=cfg.mysql['password'],
    database=cfg.mysql['database']
)

mycursor = mydb.cursor()

# Breaking lines should be neater and nicer, but threw an error; maybe come back FH
sql="CREATE TABLE vaccine ( PPSN VARCHAR(9) PRIMARY KEY, name VARCHAR(63) NOT NULL,  email VARCHAR(63) NOT NULL, age INT, location VARCHAR(255), medical BOOLEAN, occupation VARCHAR(63), stage INT, vaccinated_1 BOOLEAN, vaccinated_2 BOOLEAN);"

mycursor.execute(sql)
