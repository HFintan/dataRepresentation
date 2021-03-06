import mysql.connector
#import dbconfig as cfg

class VaccineDao:
    db=""
    def __init__(self):
    # dbconfig was giving me an error for Django after an update
    # though it had been working previously, so I abandoned it.
    #    self.db = mysql.connector.connect(
    #    host=cfg.mysql['host'],
    #    user=cfg.mysql['user'],
    #    password=cfg.mysql['password'],
    #    database=cfg.mysql['database']
    #)    
        self.db = mysql.connector.connect(
        host='localhost',
        user='fintan',
        password='password',
        database='datarepresentation'
    )


    def create(self,person):
        cursor=self.db.cursor()
#        sql = "insert into people (PPSN, name, email, age, location, medical, occupation, stage, vaccinated_1, vaccinated_2) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        sql = "insert into people (PPSN, name, email, age, location,medical, occupation, stage, vaccinated_1, vaccinated_2) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = [
            person['PPSN'],
            person['name'],
            person['email'],
            person['age'],
            person['location'],
            person['medical'],
            person['occupation'],
            person['stage'],
            person['vaccinated_1'],
            person['vaccinated_2']
        ]
        cursor.execute(sql,values) 
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = "select * from people"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        # print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
        return returnArray

    def findById(self,PPSN):
        cursor = self.db.cursor()
        sql = "select * from people where PPSN = %s"
        values = [ PPSN ]
        cursor.execute(sql,values)
        result = cursor.fetchone()
        return self.convertToDict(result)

    def update(self,person):
        cursor=self.db.cursor()
        sql = "update people set name = %s, email = %s, age = %s, location = %s, medical = %s, occupation = %s, stage = %s, vaccinated_1 = %s, vaccinated_2 = %s where PPSN = %s" 
        values = [
            person['name'],
            person['email'],
            person['age'],
            person['location'],
            person['medical'],
            person['occupation'],
            person['stage'],
            person['vaccinated_1'],
            person['vaccinated_2'],
            person['PPSN']
        ]
        cursor.execute(sql,values) 
        self.db.commit()
        return cursor.lastrowid

    def delete(self,PPSN):
        cursor = self.db.cursor()
        sql = "delete from people where PPSN = %s"
        value = [ PPSN ]
        cursor.execute(sql,value)
        return {}

    def convertToDict(self,result):
        colnames = ['PPSN','name','email','age','location','medical','occupation','stage','vaccinated_1','vaccinated_2']
        person = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                person[colName] = value
        return person

vaccineDao = VaccineDao()
