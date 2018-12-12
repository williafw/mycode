#!/usr/bin/env python3
list1 = ["cisco_nxos", "arista_eos", "cisco_ios" ]
print(list1)
list1.extend(["Juniper"]) # This is to extend the list
print(list1)
list1.append(["10.1.0.1", "10.2.0.1", "10.3.0.1" ]) # This adds to the end of the line
print(list1)
print(list1[4])  # Returns the value of 5 in list1

print([list1[4][0]])