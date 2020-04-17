import requests
import json
import jsonpath

# API URL
params = {'page': 2}
url = "https://reqres.in"

# Send GET request
response = requests.get(url+"/api/users", params=params)
#print(json.dumps(response, indent=4))
res = response.json()
id = [d['first_name'] for d in res['data']]
print(id)

# Display response content
# print(response.content)
# print(response.headers)

# Parse response to Json format
#json_response = json.loads(response.text)
# print(json_response)

# Fetch value using Json path
pages = jsonpath.jsonpath(response.json(), 'data')
#print(pages)
