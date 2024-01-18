import requests
import json

endpoint = "http://localhost:8000/api/home"

# res = requests.get(endpoint)

# print(res.json()[0]["text"])

myjson = {
    "title": "Another Random CL",
}

res = requests.post(endpoint, json= myjson)

print(res.json())