#!/usr/bin/env python3

def main():
    
    # list of 3 items
    my_list = [ "192.168.0.5", 5060, "UP" ]

    # return the first IP address
    print("The first item in the list (IP): " + my_list[0] )
    
    # return the port 5060 as string
    print("The second item in the list (port): " + str(my_list[1]) )

    # return last item
    print("The last item in the list (state): " + my_list[2] )

main()
