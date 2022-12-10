import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data=json_data)
    print(r.json())
    
get_data()
# get_data(1)


def post_data():
    data = {
        'name': 'Nitin',
        'roll': 106,
        'city': 'pune'
    }
    json_data = json.dumps(data)
    r = requests.post(url = URL, data=json_data)
    print(r.json())

# post_data()


def update_data():
    data = {
        'id' : 5,
        'name': 'nitin',
        'city': 'Pune'
    }
    json_data = json.dumps(data)
    r = requests.put(url = URL, data=json_data)
    print(r.json())

# update_data()


def delete_data():
    data = {
        'id' : 5,
    }
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data=json_data)
    print(r.json())

# delete_data()
