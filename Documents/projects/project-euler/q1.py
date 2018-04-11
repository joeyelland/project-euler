#!/usr/bin/python
i = 0 #counter
total = 0 #result

while (i < 1000): #loop through numbers below 1000
    if ((i % 3 == 0) or (i % 5 == 0)): #true if i is a multiple of 3 or 5 or both
        total += i #adds value of i to total
        i += 1 
    else:
        i += 1

print total
