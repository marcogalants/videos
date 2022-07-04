import requests, json
from videos import printlog

BASE="http://127.0.0.1:5005/"
"""
videos=[
    {"likes": 1000, "name": "how to make a microservice", "views": 23233},
    {"likes": 430, "name": "how to make a microservice", "views": 10300330},
    {"likes": 56, "name": "meet Marco", "views": 106},
    {"likes": 1945, "name": "how to become millionaire", "views": 10440000}    
]
videos=[
    {"likes": 40, "name": "selling strategies", "views": 233},
    {"likes": 433, "name": "how to be good", "views": 103003},
    {"likes": 5555, "name": "meet your hero", "views": 1000698},
    {"likes": 19, "name": "my holiday", "views": 1044}   
]
# POST - create
for i in range(len(videos)):
    # post request sends json as body of request
    response = requests.post(BASE + "video", headers={"content-type": "application/json"} ,data=json.dumps(videos[i]))
    print(response)


# GET - read
response = requests.get(BASE + "video/1", headers={"content-type": "application/json"})
print(response.json())

# PATCH - update
response = requests.patch(BASE + "video/2", headers={"content-type": "application/json"}, data=json.dumps({"likes": 100, "views": 440, "name": "My very favorite video"}))
response = requests.get(BASE + "video/2", headers={"content-type": "application/json"})
print(response.json())

response = requests.delete(BASE + "video/1", headers={"content-type": "application/json"})
print(response)
response = requests.get(BASE + "video", headers={"content-type": "application/json"})
print(response.json())
"""