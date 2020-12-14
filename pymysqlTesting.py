from pymysqlAltogether import studentDAO

#create
latestid = studentDAO.create(('mark',45))
#find by id
result = studentDAO.findById(latestid)
print(result)
#update
studentDAO.update(('Fred',21,latestid))
result=studentDAO.findById(latestid)
print(result)
#get all
allStudents=studentDAO.getAll()
for student in allStudents:
    print(student)
#delete
studentDAO.delete(latestid)
