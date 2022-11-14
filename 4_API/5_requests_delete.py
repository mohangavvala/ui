import requests


## To Delete emp
response = requests.delete('http://127.0.0.1:5000/delete', json={"CUST-2":"Balu"})

print('\n response code is :', response.status_code)
print('\n Deleted is :', response.text)

assert response.status_code == 200, 'Response status_code is not expected'
assert response.text.strip() == 'CUST-2 RECORD DELETED SUCCESSFULLY', ' Customer is not deleted'