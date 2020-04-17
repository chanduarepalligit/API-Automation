import requests
import json
import jsonpath

url = "https://reqres.in/api/users"

# Read input json file
file = open("C:\\Users\\Chandu\\Desktop\\postreq.json", 'r')

# Read Data
json_read = file.read()

# Parse file in to json
request_json = json.loads(json_read)
print(request_json)

# Make post request with input json body
response = requests.post(url, request_json)
print(response.content)
status = response.status_code
print(status)
if status == 201:
    print("Post json data successful")
else:
    print("Post json data failed")

# Fetch header from response
print("Content length is :", response.headers.get('Content-Length'))

# Parse response to json format
response_json = json.loads(response.text)
print(response_json)

# Pick id using json path
get_id = jsonpath.jsonpath(response_json, 'id')
print(get_id[0])

