#!/usr/bin/env python3
#LAB 14 IPV4 testing with if 
ipchk = "192.168.0.1"

if ipchk:
    print("Looks like the IP address was set: " + ipchk)



ipchk = input("") # this line now promts the user for input. Apply an IP address

if ipchk: # If any data is provide, this will be true
    print("Looks like the IP address was set: " + ipchk) # Indented under if

else:
    print("The IP address was not set")



ipchk = input("") # Enter IP address at the prompt
if ipchk == "192.168.70.1" :  # if a match on 192.168.70.1
    print("Looks like the IP address on the gateway was set: " + ipchk + "This is not recommended")

elif ipchk:  # if data was provided it will show here
    print("Looks like the IP address was set: " + ipchk)  # indent 4 spaces under if

else: # If there was no data provided
    print("You did not provide input")