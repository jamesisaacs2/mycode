#!/usr/bin/env python3
import requests
from pprint import pprint

URL= "http://127.0.0.1:2224/"

res = requests.get(URL).json()

pprint(res)

