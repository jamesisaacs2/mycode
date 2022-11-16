#!/usr/bin/python3

import requests

# define the URL we want to use
TIMEURL = "http://date.jsontest.com"
IPURL = "http://ip.jsontest.com"
VALIDURL = "http://validate.jsontest.com/"

def main():
    ## PART A
    ## pull a time object from date.jsontest.com
    # make the request
    resp = requests.get(TIMEURL)
    # pull json off 200 response
    # and change to PYTHONIC data
    mytime = resp.json()
    # pull out the value associated with the KEY "time"
    # then strip out all whitespaces
    # replace colons with hyphens
    mytime = mytime["time"].replace(" ", "").replace(":", "-")

    ## PART B
    ## make the request
    resp = requests.get(IPURL)
    myip = resp.json()
    print(myip)
    ## grab the value associated with the KEY "ip"
    myip = myip["ip"]

    ## PART C
    ## read a list of hosts out of a flat file
    with open("/home/student/mycode/jsontest/myservers.txt") as myfile:
        mysvrs = myfile.readlines()

    ## PART D
    # test data to validate as legal json
    # when a POST json= is replaced by the KEY "json"
    # the key "json" is mapped to a VALUE of the json to test
    # because the test item is a string, we can include whitespaces
    # format for requests to validate.testjson.com is...
    # data={"json": "json you want to validate as str"}
    jsonToTest = {}
    jsonToTest["time"] = mytime
    jsonToTest["ip"] = myip
    jsonToTest["mysvrs"] = mysvrs

    mydata = {}
    mydata["json"] = str(jsonToTest)

    ## PART E
    # use requests library to send an HTTP POST
    resp = requests.post(VALIDURL, data=mydata)

    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    respjson = resp.json()

    # display our PYTHONIC data (LIST / DICT)
    print(respjson)

    # JUST display the value of "validate"
    print(f"Is your JSON valid? {respjson['validate']}")

if __name__ == "__main__":
    main()

