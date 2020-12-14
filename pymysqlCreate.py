# Can't get privileges to work for either root or fintan,
# so I'm creating the database the normal way with root (since
# fintan isn't empowered to do that anyway) and then hopefully
# the other scripts will run with fintan as the user

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE datarepresentation")

