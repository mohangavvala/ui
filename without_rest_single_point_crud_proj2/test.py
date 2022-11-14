import requests
import json
BASE_URL='http://127.0.0.1:8000'
END_POINT='/api/'
def get_resources(id=None):
    data={}
    if id is not None:
        data={
        'id':id
        }
    resp=requests.get(BASE_URL+END_POINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
get_resources(1)
#get_resources(90)
def create_resource():
    new_std= {
    'name':'Harbjan',
    'rollno':221,
    'marks':40,
    #'marks':21,
    'gf':'rai',
    'bf':'sing'
    }
    resp=requests.post(BASE_URL+END_POINT,data=json.dumps(new_std))
    #resp=requests.post(BASE_URL+END_POINT,data=new_std)
    print(resp.status_code)
    print(resp.json())
create_resource()
def update(id):
    new_data={
    'id':id,
    'gf':'Agrwal',
    }
    resp=requests.put(BASE_URL+END_POINT,data=json.dumps(new_data))
    print(resp.status_code)
    print(resp.json())
update(3)
def delete_resource(id):
    data={
    'id':id,
    }
    r=requests.delete(BASE_URL+END_POINT,data=json.dumps(data))
    print(r.status_code)
    # print(r.text)
    print(r.json())
delete_resource(5)

