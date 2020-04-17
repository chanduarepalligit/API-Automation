import requests
from pprint import pprint
import json


resp = requests.get("https://reqres.in/api/users?page=2")
breakpoint()
pprint(resp.json())
