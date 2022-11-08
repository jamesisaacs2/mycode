#!/usr/bin/env python3

def main():
    
    # create a list containing three items
    my_list = [ "192.168.0.5", 5060, "UP" ]

    # display the first item in the list
    print("The first item in the list (IP): " + my_list[0] )

    # display the second item in the list
    print("The second item in the list (port): " + str(my_list[1]) )

    # display the third item in the list
    print("The last item in the list (state): " + my_list[2] )

    # challenge, 15
    iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

    # display only IP addresses on screen
    print("IP addresses are:\n>", iplist[3], "and", iplist[4])

main()
