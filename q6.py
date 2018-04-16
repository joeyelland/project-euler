#!/usr/bin/python

# The sum of the squares of the first ten natural numbers is, 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)2 = 552 = 3025

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

n = int(input("input n = ")) #user able to input value

def square_of_sum(n):
  a = (n*(n + 1))/2 # Formula for sum of a series up to n
  a = a**2
  return a
  
def sum_of_squares(n): #Finds the sum of square numbers
  a = range(1,101)
  b = 0
  for x in a:
    b += x**2 # Increments b with each n**2
  return b
    
  
print(square_of_sum(n) - sum_of_squares(n))
