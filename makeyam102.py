#!/usr/bin/python3

# YAML is NOT part of the standard library
import yaml

def main():
    ## create a blob of data to work with
    hitchhikers = [{"name": "Zaphod Beelebrox", "species": "Betelgeusian"}, {"name": "Arthur Dent", "species": "Human"}]

    ## display our python data (a list containing two dictinories)
    print(hitchhikers)

    ## Create the YAML string
    yamlstring = yaml.dump(hitchhikers)

    ## Display a single string of YAML
    print(yamlstring)

if __name__ == "__main__":
    main()
