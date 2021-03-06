#!/usr/bin/python

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

def prime_counter(n):
  prime_count = 0
  for i in range(1, n + 1):
    if all(i % j != 0 for j in range(2, i)):
      prime_count += 1
      print(prime_count)
      if (prime_count == 10002):
        return i
	
print(prime_counter(5000000))
