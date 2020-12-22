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

# This 12345 is hacky, but 0 and False were both giving me grief with the boolean/while loop thing
[ppsn,name,email,age,location,medical,occupation,stage,vaccinated_1,vaccinated_2] = [12345]*10 


# A valid PPSN is 7 digits followed by one or two letters, but it eventually turned out that
# this was problematic, so I just ditched the letter requirement.
while ppsn == 12345:
    value_ppsn = input('PPSN:')
 #   if re.match('[0-9]{7}[A-Za-z]{1,2}$',value_ppsn) == None:
    if re.match('[0-9]{7}$',value_ppsn) == None:
       print("A PPSN is 7 digits followed by one or two letters, BUT we've stopped including the letters because nonnumeric primary key caused problems later.")
    else:
        ppsn = int(value_ppsn)

while name == 12345:
    value_name = input('Name:')
    if re.match('[A-Za-z -]+$',value_name) == None:
        print("A valid name may be letters and spaces only.")
    else:
        name = str(value_name)

# Email regex taken from
# https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
while email == 12345:
    value_email = input('Email:')
    if re.match(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',value_email) == None:
        print("Please provide a valid email address.")
    else:
        email = str(value_email)

while age == 12345 :
    value_age = input('Age:')
    if re.match(r'\d*$',value_age) == None:
        print("Please use numbers only.")
    elif value_age == '':
        age = None
    else:
        age = str(value_age)

# Guess we'll trust the user on these
value_location = input('Local election area:')
if value_location == '':
    location = None
else:
    location = str(value_location)

while medical == 12345:
    value_medical = input('Any compromising medical conditions? y/n')  
    if re.match('(Yes|yes|YES|Y|y|True|TRUE|NO|No|no|N|n|FALSE|False)*$',value_medical) == None:
        print("I do not understand; please try again:")
    else:
        if re.match('[YyTt]+.*',value_medical):
            medical = int(1)
        elif re.match('[NnFf]+.*',value_medical):
            medical = None      # I mean, who knows really?
        else:
            medical = None

while occupation == 12345:
    value_occupation = input('Occupation:')
    if re.match('[A-Za-z -]*$',value_occupation) == None:
        print("An occupation may be letters and spaces only.")
    elif value_occupation == '':
        occupation = None
    else:
        occupation = str(value_occupation)

while stage == 12345:
        value_stage = input('Stage:')
        if re.match(r'\d*$',value_stage) == None:
            print("If provided, stage must be an integer between 1 and 15.")
        elif value_stage == '':
            stage = None
        elif 1 <= int(value_stage) <=15:
            stage = str(value_stage)
        else:
            print("If provided, stage must be an integer between 1 and 15.")

while vaccinated_1 == 12345:
    value_vaccinated_1 = input('Had first vaccination? y/n. If unknown, leave blank.')
    if re.match('(Yes|yes|YES|Y|y|True|TRUE|NO|No|no|N|n|FALSE|False)*$',value_vaccinated_1) == None:
        print("I do not understand; please try again:")
    else:
        if re.match('[YyTt]+.*',value_vaccinated_1):
            vaccinated_1 = int(1)
            while vaccinated_2 == 12345:
                value_vaccinated_2 = input('Had second vaccination? y/n. If unknown, leave blank.')
                if re.match('(Yes|yes|YES|Y|y|True|TRUE|NO|No|no|N|n|FALSE|False)*$',value_vaccinated_2) == None:
                    print("I do not understand; please try again:")
                else:
                    if re.match('[YyTt]+.*',value_vaccinated_2):
                        vaccinated_2 = int(1)
                    elif re.match('[NnFf]+.*',value_vaccinated_2):
                        vaccinated_2 = int(0)
                    else:
                        vaccinated_2 = None
        elif re.match('[NnFf]+.*',value_vaccinated_1):
            vaccinated_1 = int(0)
            vaccinated_2 = int(0)
        else:
            vaccinated_1 = None
            vaccinated_2 = None

 
print(ppsn,name,age,email,location,occupation,stage,vaccinated_1,vaccinated_2) 
cursor = mydb.cursor()
sql = "insert into people (ppsn,name,email,age,location,medical,occupation,stage,vaccinated_1,vaccinated_2) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
values = (ppsn,name,email,age,location,medical,occupation,stage,vaccinated_1,vaccinated_2)

cursor.execute(sql,values)

mydb.commit()
print("1 record inserted, ID:", cursor.lastrowid)
