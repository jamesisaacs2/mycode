#!/usr/bin/python3

def main():

    # lists provided
    # 0,1 - string ; 2 - sublist ; 3 - nothing
    challenge = ["science", "turbo", ["goggles", "eyes"], "nothing"]
    cEyes = challenge[2][1]
    cGoggles = challenge[2][0]
    cNothing = challenge[-1]

    print(f"My {cEyes}! The {cGoggles} do {cNothing}!")

    # 0,1 - string ; 2 - dictionary ; 3 - nothing
    trial = ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
    tEyes = trial[2]["goggles"]
    tGoggles = trial[2]["eyes"]
    tNothing = trial[-1]

    print(f"My {tEyes}! The {tGoggles} do {tNothing}!")

    # 0 - dict obj ; 1, 2 - dict
    nightmare = [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]
    nEyes = nightmare[0]["user"]["name"]["first"]
    nGoggles = nightmare[0]["kumquat"]
    nNothing = nightmare[0]["d"]

    print(f"My {nEyes}! The {nGoggles} do {nNothing}!")
    
main()
