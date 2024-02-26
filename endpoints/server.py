""" A simple flask app that handles CRUD """
from flask import Flask, make_response, request

app = Flask(__name__)

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]

@app.route("/data")
def get_data():
    """ This checks whether there is any data stored"""
    try:
        if data and len(data) > 0:
            return {"message": f"Data of length {len(data)} found"}
        return {"message": "Data is empty"}, 500
    except NameError:
        return {"message": "Data not found"}, 404

@app.route("/name_search")
def name_search():
    """ searches for the name given in the url parameters """
    fr_name = request.args.get("q")
    if not fr_name:
        return ({"message": "Invalid input parameter"}, 422)
    for person in data:
        #if person["first_name"] == fr_name: -mine
        if fr_name.lower() in person["first_name"].lower():
            return person, 200
    return ({"message": "Person not found"}, 404)

@app.route("/count")
def count():
    """ counts the number of people stored """
    try:
        people_ct = len(data)
        return {"Data count": people_ct}, 200
    except NameError:
        return {"message": "Data not defined"}, 500

@app.route("/person/<uuid:uniq_id>")
def find_by_uuid(uniq_id):
    """ Searches for the person with the given UUID """
    for person in data:
        if str(uniq_id) == person["id"]:
            return person, 200
    return ({"message": "Person not found"}, 404)

@app.route("/person/<uuid:uniq_id>", methods=["DELETE"])
def delete_by_uuid(uniq_id):
    """ Deletes the person with the given uuid """
    for person in data:
        if str(uniq_id) == person["id"]:
            data.remove(person)
            return {"message": f"Person of id {uniq_id} has been deleted successifully."}, 200
    return ({"message": "Person not found"}, 404)

@app.route("/person", methods=["POST"])
def add_by_uuid():
    """ Recieves a person object and adds the person to the storage """
    new_person = request.json
    if not new_person:
        return ({"message": "Invalid input parameter"}, 422)
    try:
        data.append(new_person)
    except NameError:
        return {"message": "Data not defined"}, 500

    return {"message": new_person["id"]}, 200

"""
## Sample data to add
curl -X POST -i -w '\n' \
  --url http://localhost:5000/person \
  --header 'Content-Type: application/json' \
  --data '{
        "id": "4e1e61b4-8a27-11ed-a1eb-0242ac120002",
        "first_name": "John",
        "last_name": "Horne",
        "graduation_year": 2001,
        "address": "1 hill drive",
        "city": "Atlanta",
        "zip": "30339",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff"
}'
"""

@app.errorhandler(404)
def api_not_found(error):
    """ Handles the 404 error
    returns json instead of the default html template.
    """
    return {"message": "Api not found"}, 404
@app.route("/no_content")
def no_content():
    """ no content """
    return "No content found", 204

@app.route("/exp")
def index_explicit():
    """ How to use a response object instead """
    resp = make_response({"message": "Hello world"})
    resp.status_code = 200
    return resp
