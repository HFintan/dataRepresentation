import mysql.connector
import re
import dbconfig as cfg

mydb = mysql.connector.connect(
    host=cfg.mysql['host'],
    user=cfg.mysql['user'],
    password=cfg.mysql['password'],
    database=cfg.mysql['database']
)

# This works, but requires more lines than multiple while loops,
# and there's no obvious benefit, so we'll keep it simple.
#value_ppsn = False; value_name = False
#while not (value_ppsn != False and value_name != False):
#    if value_ppsn == False:
#        value_ppsn = input('PPSN:')
#        if re.match('[0-9]{7}[A-Za-z]{1,2}$',value_ppsn) == None:
#            print("A valid PPSN is 7 digits followed by one or two letters.")
#            value_ppsn = False
#        else:
#            ppsn = str(value_ppsn)
#    
#    if value_name == False:
#        value_name = input('Name:')
#        if re.match('[A-Za-z -]+$',value_name) == None:
#            print("A name may be letters and spaces only.")
#            value_name = False
#        else:
#            name = str(value_name)

# Using 0 because False is needed as return value for vaccinated_1/2 
[ppsn,name,age,email,lea,occupation,stage,vaccinated_1,vaccinated_2] = [0]*9; 

while ppsn == 0:
    value_ppsn = input('PPSN:')
    if re.match('[0-9]{7}[A-Za-z]{1,2}$',value_ppsn) == None:
        print("A valid PPSN is 7 digits followed by one or two letters.")
    else:
        ppsn = str(value_ppsn)

while name == 0:
    value_name = input('Name:')
    if re.match('[A-Za-z -]+$',value_name) == None:
        print("A valid name may be letters and spaces only.")
    else:
        name = str(value_name)

while age == 0 :
    value_age = input('Age:')
    if re.match('\d*$',value_age) == None:
        print("Please use numbers only.")
    else:
        age = str(value_age)

# Email regex taken from
# https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
while email == 0:
    value_email = input('Email:')
    if re.match('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',value_email) == None:
        print("Please provide a valid email address.")
    else:
        email = str(value_email)

# Guess we'll trust the user on these
lea = input('Local election area:')

while occupation == 0:
    value_occupation = input('Occupation:')
    if re.match('[A-Za-z -]*$',value_occupation) == None:
        print("An occupation may be letters and spaces only.")
    else:
        occupation = str(value_occupation)

while stage == 0:
        value_stage = input('Stage:')
        if re.match('\d*$',value_stage) == None:
            print("If provided, stage must be an integer between 1 and 12.")
        elif value_stage == '':
            stage = ''
        elif 1 <= int(value_stage) <=12:
            stage = str(value_stage)
        else:
            print("If provided, stage must be an integer between 1 and 12.")

while vaccinated_1 == 0:
    value_vaccinated_1 = input('Had first vaccination? y/n. If unknown, leave blank.')
    if re.match('(Yes|yes|YES|Y|y|True|TRUE|NO|No|no|N|n|FALSE|False)*$',value_vaccinated_1) == None:
        print("I do not understand; please try again:")
    else:
        if re.match('[YyTt]+.*',value_vaccinated_1):
            vaccinated_1 = 'True'
        elif re.match('[NnFf]+.*',value_vaccinated_1):
            vaccinated_1 = 'False'
        else:
            vaccinated_1 = ''

while vaccinated_2 == 0:
    value_vaccinated_2 = input('Had first vaccination? y/n. If unknown, leave blank.')
    if re.match('(Yes|yes|YES|Y|y|True|TRUE|NO|No|no|N|n|FALSE|False)*$',value_vaccinated_2) == None:
        print("I do not understand; please try again:")
    else:
        if re.match('[YyTt]+.*',value_vaccinated_2):
            vaccinated_2 = 'True'
        elif re.match('[NnFf]+.*',value_vaccinated_2):
            vaccinated_2 = 'False'
        else:
            vaccinated_2 = ''
 
print(ppsn,name,age,email,lea,occupation,stage,vaccinated_1,vaccinated_2) 
cursor = db.cursor()
sql = "insert into vaccine (ppsn,name,age,email,lea,occupation,stage,vaccinated_1,vaccinated_2) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
values = (ppsn,name,age,lea,occupation,stage,vaccinated_1,vaccinated_2)

cursor.execute(sql,values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)
