#!/usr/bin/env python3
hostname = "MTG"
if hostname == ("MTG"):
    print("The hostname was found to be MTG")

hostname = "Input data from the user"
if hostname == ("Input data from the user"):
   print("May we have your input data?")

hostname = "mtg", "MTG", "mTG", "MTg", "mTG", "MtG"
if hostname == ("mtg", "MTG", "mTG", "MTg", "mTG", "MtG"): # The user can receive data in any order
    print("The user can enter data in any order")
    print("hostname matches expected config")
   
 