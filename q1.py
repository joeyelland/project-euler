#!/usr/bin/python

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

i = 0 #counter
total = 0 #result

while (i < 1000): #loop through numbers below 1000
    if ((i % 3 == 0) or (i % 5 == 0)): #true if i is a multiple of 3 or 5 or both
        total += i #adds value of i to total
        i += 1
    else:
        i += 1

print total
