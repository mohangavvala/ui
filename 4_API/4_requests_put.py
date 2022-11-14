import requests

## To Update emp 
response = requests.put('http://127.0.0.1:5000/update', json={"CUST-1":"SRIRAM"})

print('\n response code is :', response.status_code)
print('\n update is :', response.text)

assert response.status_code == 200, 'Response status_code is not expected'
assert response.text.strip() == 'CUST-1 RECORD UPDATED SUCCESSFULLY', ' Customer name is not updated '

