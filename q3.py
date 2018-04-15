#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#!/usr/bin/python
factors = []
prime_factors = []
n = int(input("input n = "))

def find_factors(value): #Lists factors of value
	i = 1
  	while (i <= value):
		if (value % i == 0):
			factors.append(i)
	  		print factors[i - 1]
		i += 1
 	return factors

def find_largest_prime(factors):
	for i in factors:
		if all(i % j != 0 for j in range(2,i)):
			prime_factors.append(i)
		else:
			pass
	return max(prime_factors)

print find_largest_prime(find_factors(n))
