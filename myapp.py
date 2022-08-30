from operator import truediv
import requests, json

url = "http://127.0.0.1:8000/api/student-list/"

def get_Data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
        json_data = json.dumps(data)
        r = requests.get(url=url,data=json_data)
        data = r.json()
        print(data)
    else:
        json_data = json.dumps(data)
        r = requests.get(url=url,data=json_data)
        data = r.json()
        print(data)

# if don't pass any parameter or id then we get every records
# get_Data(2)


def post_data():
    data = {
        'name' : 'Komal',
        'city': 'Karachi',
        'rollNo': 456
    }
    json_data = json.dumps(data)
    r = requests.post(url,json_data)
    data = r.json()
    print(data)

post_data()

def update_data():
    data = {
        'id': 4,
        'name' : 'Asif',
        'city': 'Lahore',
    }
    json_data = json.dumps(data)
    r = requests.put(url,json_data)
    data = r.json()
    print(data)

# update_data()


def delete_data():
    data = {'id':2}
    json_data = json.dumps(data)
    r = requests.delete(url,json_data)
    data = r.json()
    print(data)

# delete_data()