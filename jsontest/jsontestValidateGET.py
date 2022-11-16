#!/usr/bin/python3

import requests
import json

# define the URL we want to use
GETURL = "http://validate.jsontest.com/"

def main():
    # test data to validate as legal json
    mydata = {"fruit": ["apple", "pear"], "vegetable": ["carrot"]}

    ## the next two lines do the same thing
    ## we take python, convert to a string, then strip out whitespace
    #jsonToValidate = "json=" + str(mydata).replace(" ", "")
    #jsonToValidate = f"json={ str(mydata).replace(' ', '') }"
    ## slightly different thinking
    ## user json library to convert to legal json, then strip out whitespace
    jsonToValidate = f"json={ json.dumps(mydata).replace(' ', '') }"

    # use requests library to send an HTTP GET
    resp = requests.get(f"{GETURL}?{jsonToValidate}")

    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    respjson = resp.json()

    # display our PYTHONIC data (LIST / DICT)
    print(respjson)

    # JUST display the value of "validate"
    print(f"Is your JSON valid? {respjson['validate']}")

if __name__ == "__main__":
    main()

