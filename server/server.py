from flask import Flask, url_for, request, redirect, abort, jsonify
from vaccineDao import vaccineDao

app = Flask(__name__, static_url_path='', static_folder='staticpages')


@app.route('/')
def index():
    return "hello"
#get all
# curl Http://127.0.0.1:5000/people
@app.route('/people')
def getAll():
    return jsonify(vaccineDao.getAll())

# find By id
# curl Http://127.0.0.1:5000/people/2
@app.route('/people/<int:PPSN>')
def findById(PPSN):
    return jsonify(vaccineDao.findById(PPSN))

# This one works
# curl -X POST -d "{\"PPSN\":10,\"name\":\"Is location a problem?\",\"email\":\"test@gmail.com\",\"age\":null,\"location\":null,\"medical\":null,\"occupation\":\"waster\",\"stage\":6,\"vaccinated_1\":null,\"vaccinated_2\":null}" -H Content-Type:application/json http://127.0.0.1:5000/people
@app.route('/people', methods=['POST'])
def create():
    if not request.json:
        abort(400)
    person = {
        'PPSN': request.json['PPSN'],
        'name': request.json['name'],
        'email': request.json['email'],
        'age': request.json['age'],
        'location': request.json['location'],
        'medical': request.json['medical'],
        'occupation': request.json["occupation"],
        'stage': request.json['stage'],
        'vaccinated_1': request.json['vaccinated_1'],
        'vaccinated_2': request.json['vaccinated_2']
    }
    return jsonify(vaccineDao.create(person))


    return "served by Create "

#update curl -X PUT -d "{\"name\":\"That's not my name\", \"age\":\"42\"}" -H "content-type:application/json" http://127.0.0.1:5000/people/1
@app.route('/people/<int:PPSN>', methods=['PUT'])
def update(PPSN):
    foundPerson = vaccineDao.findById(PPSN)
    print (foundPerson)
    if foundPerson == {}:
        return jsonify({}), 404
    currentPerson = foundPerson
    if 'name' in request.json:
        currentPerson['name'] = request.json['name']
    if 'email' in request.json:
        currentPerson['email'] = request.json['email']
    if 'age' in request.json:
        currentPerson['age'] = request.json['age']
    if 'location' in request.json:
        currentPerson['location'] = request.json['location']
    if 'medical' in request.json:
        currentPerson['medical'] = request.json['medical']
    if 'occupation' in request.json:
        currentPerson['occupation'] = request.json['occupation']
    if 'stage' in request.json:
        currentPerson['stage'] = request.json['stage']
    if 'vaccinated_1' in request.json:
        currentPerson['vaccinated_1'] = request.json['vaccinated_1']
    if 'vaccinated_2' in request.json:
        currentPerson['vaccinated_2'] = request.json['vaccinated_2']
    vaccineDao.update(currentPerson)
    return jsonify(currentPerson)

#delete
# curl -X DELETE http://127.0.0.1:5000/people/2
@app.route('/people/<int:PPSN>', methods=['DELETE'])
def delete(PPSN):
    vaccineDao.delete(PPSN)
    return jsonify({"done":True})


if __name__ == "__main__":
    app.run(debug=True)
