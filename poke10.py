#!/usr/bin/python3

# this is for pretty printing
import pprint

import requests

POKEMONAPI = "https://pokeapi.co/api/v2/pokemon/rattata/"

def main():
   # go grab ALL the info from the API
    poke = requests.get(POKEMONAPI)
    # strip off the JSON from the API
    pokejson = poke.json()

     # Loop across JUST the moves
    for abl in pokejson["moves"]:
    #print JUST the move name
     print(abl["move"]["name"])

if __name__ == "__main__":
        main()
