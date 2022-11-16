#!/usr/bin/python3

import requests

# define the URL we want to use
IPURL = "http://ip.jsontest.com/"

def main():
    # use requests library to send an HTTP GET
    resp = requests.get(IPURL)

    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    respjson = resp.json()

    # display our PYTHONIC data (LIST / DICT)
    print(respjson)

    # JUST display the value of "ip"
    print(f"The current WAN IP is --> {respjson['ip']}")

if __name__ == "__main__":
    main()

