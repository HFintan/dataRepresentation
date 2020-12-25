# dataRepresentation
DR module for gmithdip


########################### Contents ########################
# ProjectCreateTable.py
Creates a specified table in the datarepresentation database.
(ignorable)

# ProjectInsert.py
Prompts user for details and inserts them into the Table. 
Regexes pickier than for json/html will be.
(ignorable, unless you want better input restriction regexes) 

#init.sql
An initial file with some data, created with
sudo mysqldump -u root datarepresentation > init.sql

can be imported (possibly after creating the empty database datarepresentation) using
sudo mysql -u root -p datarepresentation < init.sql

#requirements.txt
A list of the required modules

#configtemplate and dbconfig.py
These worked until I ran an update on something, and then there was an issue with 
django settings which I could not find a suitable fix for, so I abandoned it and
just hardcoded the parameters in vaccineDAO.py, which may, unfortunately, need to be adjusted.

I've granted all privileges on the database
grant all privileges on *.* to ''@'localhost' identified by 'password' with grant option;

#OLSapp.py
For failed attempts to moving to pythonanywhere; mysql part gave too much grief.
(ignorable)


The directory SERVER contains the three files requested for this project:
# vaccineDAO.py
# app.py (was server.py)
# staticpages/index.html


############################## TO RUN ########################
0. Possibly adjust the mysql parameters in vaccineDAO.py, unfortunately.
0. There's nothing unusual in requirements.txt; flask and mysql-connector.
0. Import init.sql into mysql as outlined above for sample entries
1. cd server
2. flask run
3. Go to index.html and mess around. Individuals stored at 127.0.0.1:5000/people etc.

########################### "Quirks" #########################
html Sometimes needs refreshing after update.
The database within mysql does not update after a delete, but the deleted
entries are gone after the next create is run.

