#!/usr/bin/python3
"""Shreeja B. Google API project"""

# imports from standard library
from pprint import pprint
import json
import time

# python -m pip install requests
import requests

# Define Globals (my API key is my global variable)
APIKEYLOC = r"C:\Users\Student\Desktop\googleapi.txt"
with open(APIKEYLOC, "r") as mykey:
    APIKEY = mykey.read()

# Display what we think the API key currently is (test purposes only)
# commented out as we are correctly harvesting our key
# print(APIKEY)

def findPlaces(loc,radius=3000,pagetoken=None):
   ## pull lat and lon from loc ( passed to findPlaces within main() )
   lat, lng = loc

   ## the TYPE of place to look up
   ## a list of place TYPES are avail @ https://developers.google.com/places/supported_types
   type = "restaurant"

   ## if pagetoken does NOT have a value
   if not pagetoken:
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&type={type}&key={APIKEY}".format(lat=lat, lng=lng, radius=radius, type=type, APIKEY=APIKEY)
   else:
       url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&type={type}&key={APIKEY}{pagetoken}".format(lat=lat, lng=lng, radius=radius, type=type, APIKEY=APIKEY, pagetoken="&pagetoken="+pagetoken)


   ## display the API we lookup
   ## test purposes ONLY to be commented out on final run
   print(url)

   ## make request to URL
   response = requests.get(url)

   ## pull JSON off of response
   res = json.loads(response.text)

   ## display JSON response on screen with pretty print
   pprint(res)

   ## parse out response and create strings of the results
   for result in res["results"]:
      info = ";".join(map(str,[result["name"],
                               result["geometry"]["location"]["lat"],
                               result["geometry"]["location"]["lng"],
                               result.get("rating",0)]))
      # displays single line of results to the screen
      print(info)

   # try to harvest a pagetoken if it exists, if it does not, return None
   pagetoken = res.get("next_page_token", None)
   return pagetoken


# Runtime code that invokes the functions I created
def main():
    # tuple representing the lat and lon of Tacoma
    tacloc = ("47.2529","-122.4443")


    userchoice = input("do you want to pick your own location? (no / yes)").lower()
    if userchoice == "no" or userchoice == "n":
        pprint(tacloc)
    elif userchoice == "yes" or userchoice == "y":
        lat = input("What is your latitude value: ")
        lon = input("What is your longitude value: ")
        tacloc = (lat, lon)
    else:
        print("That is not a valid selection")
        exit()

    pagetoken = None

    while True:
         pagetoken = findPlaces(loc=tacloc, pagetoken=pagetoken)
         time.sleep(2)

         ## if there is NOT a pagetoken returned, then there is no more data to look at
         ## therefore we can break out of our while True logic
         if pagetoken == "None":
             break

         ## does the user want to continue their lookup
         userchoice = input("Looks like even MORE data is available! Do you want to look at the second page of results? (NO / yes)")
         if userchoice == "":
             break

         ## force userchoice to be lowercase
         userchoice = userchoice.lower()
         ## determine if a n or no was passed
         if userchoice == "n" or userchoice == "no":
             break

print("Successful lookup using Google APIs!")

if __name__ == "__main__":
    main()
