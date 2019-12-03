#!/usr/bin/python3

def main():
    ## a lsit of atlas3 classes
    alta3classes = ["pyhotn_basics", "python_api_design", "python_for_networking", "kubernetes", "sip", "ims", "4g", "avaya", "ansible", "python_and_ansible_for_network_automation"]

    ## display the list
    print(alta3classes)

    ##how long is the list use the built in len functions
    ## THEN print (display) the results
    print(len(alta3classes))

    # display python_basics
    print(alta3classes[0])

    # display SIP
    print(alta3classes[4])

    # display Ansible
    print(alta3classes[9])


    print(alta3classes[0:3])

    print(alta3classes[2:5])

    print(alta3classes[-1])

if __name__ == "__main__":
    main()
