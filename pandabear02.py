#!/usr/bin/python3

import pandas as pd
import json


def main():
    ciscocsv = pd.read_csv("ciscodata.csv")
    ciscojson = pd.read_json("ciscodata2.json")

    # display frist 5 entries of the ciscocsv dataframe
    print(ciscocsv.head())

    # display frist 5 entries of the ciscojson dataframe
    print(ciscojson.head())

    ciscodf = pd.concat([ciscocsv, ciscojson])
    # uncoment the line below to "fix" the index issue
    # ciscodf = pd.cocat([ciscocsv, ciscojson] , ignore_index=True , sort=False)

    print(ciscodf)

if __name__ == "__main__":
    main()
