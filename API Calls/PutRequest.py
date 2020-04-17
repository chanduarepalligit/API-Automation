import requests
import json
import jsonpath

url = "https://reqres.in/api/users/2"
file = open("C:\\Users\\Chandu\\Desktop\\postreq.json", 'r')
json_read = file.read()
request_json = json.loads(json_read)
response = requests.put(url, request_json)
if response.status_code == 200:
    print("Data updated successfully")
else:
    print("Data updating failed ")

response_json = json.loads(response.text)
print(response_json)
updated = jsonpath.jsonpath(response_json, 'updatedAt')
print(updated[0])
