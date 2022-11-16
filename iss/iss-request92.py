#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests

URL= "http://api.open-notify.org/iss-now.json"
def main():
    res = requests.get(URL).json()
    print(res)

    # get lat long
    lat = res["iss_position"]["latitude"]
    long = res["iss_position"]["longitude"]

    print(f""" 
        CURRENT LOCATION OF THE ISS IS:
        Latitude: {lat}
        Longitute: {long}
    """)

if __name__ == "__main__":
    main()


