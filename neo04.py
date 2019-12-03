#!/usr/bin/python3

import json
import urllib.request

NEO = "https://api.nasa.gov/neo/rest/v1/feed?api_key="

def main():
    ## get my API key - first  r is RAW String and the second r is READ only
    with open(r"C:\Users\Student\Documents\apikey.txt", "r") as nc:
        myapikey = nc.read()

       ## make a request to NEO and save as resp as neoresp
    neoresp = urllib.request.urlopen(NEO+myapikey)
    ## strip off ATTACHED json data and save as neojson
    neojson = neoresp.read() .decode("utf-8")
  ## what the heck is neo json?
    print(type(neojson))    ## this returns bytes UNTIL we .decode
                            ## now it is returning STR

    neopy = json.loads(neojson)  ## translates to dict

    for astroids in neopy["near_earth_objects"] ["2019-12-08"]:
        print(astroids["id"])
        print(astroids["name"])
        print("The Hunam name is: ", astroids["name"])

        print("The Astronomical ID is: ", astroids["id"])
        print()

        print(astroids["absolute_magnitude_h"])
        print("The absolute magnitude is:", astroids["absolute_magnitude_h"])
        print(astroids["estimated_diameter"]["miles"])
        print("The estimated diameter in miles: ", astroids["estimated_diameter"]["miles"])





        print(type(neopy))

        print(neojson)


if __name__ == "__main__":
    main()
