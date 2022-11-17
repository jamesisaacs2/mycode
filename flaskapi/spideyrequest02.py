#!/usr/bin/env python3
import requests
import json
from pprint import pprint

URL = "http://127.0.0.1:2224/"

new_hero = {
    "name": "Wolverine",
    "realName": "James Howlett",
    "since": 1974,
    "powers": ["adamantium skeleton", "claws", "regeneration"]
}

# json.dumps takes a python object and returns it as a JSON string
new_hero = json.dumps(new_hero)

# requests.post requires two arguments a the minimum
# a url to send the request
# and a json string to attach to the request
res = requests.post(URL, json=new_hero)

# pretty-print the response back from our POST request
pprint(res.json())

