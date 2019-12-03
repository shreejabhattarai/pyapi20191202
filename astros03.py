#!/usr/bin/python3

ASTROS = {"people": [{"name": "Christina Koch", "craft": "ISS"}, {"name": "Alexander Skvortsov", "craft": "ISS"}, {"name": "Luca Parmitano", "craft": "ISS"}, {"name": "Andrew Morgan", "craft": "ISS"}, {"name": "Oleg Skripochka", "craft": "ISS"}, {"name": "Jessica Meir", "craft": "ISS"}], "number": 6, "message": "success"}

def main():
    ## you write code under here
      print (ASTROS["people"])
      print (ASTROS["people"][0]["name"])
     ## display Alexander
      print(ASTROS["people"][1]["name"])
      print(ASTROS["people"][2]["name"])
      print(ASTROS["people"][3]["name"])
      print(ASTROS["people"][4]["name"])
      print(ASTROS["people"][5]["name"])

if __name__ == "__main__":
    main()
    
     ## intro to looping
for poi in ASTROS["people"]:
         print(poi["name"], "is riding on the", poi["craft"])

if __name__ == "main__":
    main()
