#!/usr/bin/python

def find_palindrome(n): #Outputs true if number is a palindrome
    num = str(n)
    if (num == num[::-1]): #Checks if the number is a palindrome
        return True
    else:
        return False

def product_check(n): # Runs through all possible 3-digits combinations until n is found
    for x in range(999,100,-1):
        for y in range(x, 100, -1):
            if(x * y == n):
                return True

def find_largest_num (n):
    x = 999 * 999 # Largest product of 3-digit numbers
    y = 99 * 99 # ;Largest product of 2-digit numbers
    while (x > y):
        if (find_palindrome(n) and product_check(n)):
            return n
        else:
            n = n - 1
            x = x - 1

print find_largest_num(999 * 999)
