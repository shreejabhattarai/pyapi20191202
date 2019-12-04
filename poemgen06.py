#!/usr/bin/python3

# import json
import json
# import random to randomly select a poem from our pythonic data
import random

## open my poem database (poems.json)
with open("poems.json") as pj:
    pythonpoems = json.load(pj)   ## convert poems.json to pythonic structure
## convert poems.json data to pythonic data
## I think i can do this with import json

## randomly selected poem from the pythonic data
print(random.choice(list(pythonpoems.values())))
## I think I can do this with import random

##print the randomly selected poem to the screen
