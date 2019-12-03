#!/usr/bin/python3

def main():
    ## create a list already containing IP address (strings)
    iplist = ["10.0.0.1", "10.0.1.1", "10.3.2.1"]

    ## create a list of ports (strings)
    iplist2 = ["5060", "80", "22"]

    ## display list
    print(iplist)

    ## use the extend method on iplist, our list object
    ## extend iterates over each 'thing' it is passed, and adds them to a list objects
    iplist.extend(iplist2)

    ## show how iplist has changed
    print(iplist)

if __name__ == "__main__":
    main()
