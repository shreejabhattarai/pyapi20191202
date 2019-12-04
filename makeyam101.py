#!/usr/bin/python3

# YAML is NOT a part of the standard library
import yaml

def main():
    ## create a blob of data to work with
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}, {"name": "Arthur Dent", "species": "Human"}]

    ## dispaly our Python data (a list containing two directionaries)
    print(hitchhikers)

    ## open a new file im write mode
    with open("galaxyguide.yaml", "w") as zfile:

        ## use the YAML library
        ## USAGE: yaml.dump(input data, file like object)
        ## unlike JSON, the YAML lib  uses .dump() to
        ## create YAML strings and write to flies
        ## the JSON lib uses .dump() to create a string and .dumps() to write to files
        yaml.dump(hitchhikers, zfile)
if __name__ == "__main__":
    main()




