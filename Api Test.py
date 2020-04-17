import requests
from pprint import pprint
import json


resp = requests.get("https://reqres.in/api/users?page=2")
pprint(resp.json())
resp_code = resp.status_code
print(resp_code)
if resp_code == 200:
    print("Response fetched")
else:
    print("Failed to fetch response")
pprint(resp.content)