#!/usr/bin/python

n = str(int(input("input n = ")))

def find_palindrome(n): #Outputs true if number is a palindrome
    num = str(n)
    if (num == num[::-1]):
        return True
    else:
        return False

print find_palindrome(n)

'''def find_largest_num (n):
    x = 999 * 999 # Largest product of 3-digit numbers
    while (x > (99 * 99)):
        if (find_palindrome(n)):
            #find factors
        else:
            x -= 1
    return n'''
