import requests
import json
import jsonpath


def test_add_new_data():
    studurl = "http://thetestingworldapi.com/api/studentsDetails"
    file = open("C:\\Users\\Chandu\\Desktop\\postreq.json", 'r')
    request_json = json.loads(file.read())
    response = requests.post(studurl, request_json)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

    tech_url = "http://thetestingworldapi.com/api/technicalskills"
    file = open("C:\\Users\\Chandu\\Desktop\\TechDetails.json", 'r')
    request_json = json.loads(file.read())
    request_json['id'] = int(id[0])
    request_json['st_id'] = id[0]
    response = requests.post(tech_url, request_json)
    print(response.text)

    add_url = "http://thetestingworldapi.com/api/addresses"
    file = open("C:\\Users\\Chandu\\Desktop\\address.json", 'r')
    request_json = json.loads(file.read())
    request_json['id'] = int(id[0])
    request_json['st_id'] = id[0]
    response = requests.post(add_url, request_json)
    print(response.text)

    final_details = "http://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response = requests.get(final_details)
    print(response.text)