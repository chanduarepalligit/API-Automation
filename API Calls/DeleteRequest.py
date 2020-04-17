import requests

url = "https://reqres.in/api/users/2"
response = requests.delete(url)
resp = response.status_code
if resp == 204:
    print("Status code success :", resp)
print(response.status_code)
