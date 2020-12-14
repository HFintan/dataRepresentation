import mysql.connector
import dbconfig as cfg

mydb = mysql.connector.connect(
    host=cfg.mysql['host'],
    user=cfg.mysql['username'],
    password=cfg.mysql['password'],
    database=cfg.mysql['database']
)

mycursor = mydb.cursor()

sql="CREATE TABLE vaccine (
    PPSN VARCHAR(9) PRIMARY KEY, 
    name VARCHAR(63) NOT NULL, 
    age INT NOT NULL, 
    location VARCHAR(255)),
    job VARCHAR(63),
    stage INT, 
    vaccinated BOOLEAN
);"

mycursor.execute(sql)
