#!/usr/bin/python3

def main():
   ## create an empty list
    mylist =[]

   ## open a SLOT at th END of the list to ADD the values.
    mylist.append("monday")

    mylist.append("tuesday")

    mylist.append("wednesday")

    mylist.append("thursday")
    print(mylist)
   ## print Monday on the screen
    print(mylist[0])
   ## print Thursday on the screen
    print(mylist[3])

if __name__ == "__main__":
    main()

   ## create an empty dictionary
    studiomovies = {}

    ## we want to create the KEY pixar and map to a value
    studiomovies["pixar"] = "toystory"

    studiomovies["unoversal"] = "jaws"

    studiomovies["paramount"] = "raiders of lost ark"

    print(studiomovies)
   ## print only raiders of lost arc
    print(studiomovies["paramount"])

    # map studiomovies pixar to lIST that has TWO items in it
    studiomovies["pixar"] = ["toystory" , "up"]

   ## print only UP
    print(studiomovies["pixar"][1])

