from vaccineDao import vaccineDao
print('ok')

person1 = {
        'PPSN': '9876543M',
        'name': 'Changed to person',
        'email': 'godsavethe@queen.com',
        'age': 45,
        'location':'NULL',
        "medical": None,
        'occupation': 'musician',
        'stage': 2,
        'vaccinated_1':0,
        'vaccinated_2':None
}

person2 = {
        'PPSN': '9876543M',
        'name': 'Changed to person',
        'email': 'godsavethe@queen.com',
        'age': 999,
        'location':'NULL',
        "medical": None,
        'occupation': 'musician',
        'stage': 12,
        'vaccinated_1':0,
        'vaccinated_2':None
}

#returnValue = vaccineDao.create(person)
returnValue = vaccineDao.getAll()
print(returnValue)
print('find By Id')
returnValue = vaccineDao.findById(person2['PPSN'])
print(returnValue)
print('update\n')
returnValue = vaccineDao.update(person2)
print(returnValue)
print('find By Id')
returnValue = vaccineDao.findById(person2['PPSN'])
print(returnValue)
returnValue = vaccineDao.delete(person2['PPSN'])
print(returnValue)
returnValue = vaccineDao.getAll()
print(returnValue)
