#!/usr/bin/python

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def find_num(n):
  while 0 < n:
    if all(n % m == 0 for m in range(1, 21)):
      return n 
    else:
      n += 1

print(find_num(2520))
