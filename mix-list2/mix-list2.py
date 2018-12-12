#!/usr/bin/env python3
proto = [ "ssh", "http", "https" ]
protoa = [ "ssh", "http", "https" ]
print(proto)  
print(proto [1]) # The first number in a list is always indexed at 0.
proto.append("dns") # This line will add "dns" to the end of the list
protoa.append("dns") # This line will add "dns" to the end of the list
print(proto)
proto2 = [22, 80, 443, 53] # List of common ports
proto.extend(proto2) # Pass proto2 as an argument to the extend method..then print result
print(proto)

protoa.append(proto2) # Pass proto2 as an argument to the append method
print(protoa)