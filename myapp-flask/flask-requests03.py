#!/usr/bin/env python3

import requests
import json
from pprint import pprint

URL = "http://127.0.0.1:2224/jason"

new_mensch = {
    "name": "Dovid",
    "realname": "Rabbi Dovid Meyer OBM",
    "since": 1954,
    "foods": ["bagels", "lox", "gefilte fish"]
}

# json.dumps takes a python object and returns it as a JSON string
new_mensch = json.dumps(new_mensch)

# requests.post requires two arguments at the minimum;
# a url to send the request
# and a json string to attach to the request
res = requests.post(URL, json=new_mensch)

# pretty-print the response back from our POST request
pprint(res.json())
