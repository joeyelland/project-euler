#!/usr/bin/python

#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

digits = '''73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450'''

def find_adjacent(n, i):
	cond_1 = int(n[i])
	cond_2 = int(n[i - 1]) + 1
	cond_3 = int(n[i - 1]) - 1
	cond_4 = int(n[i - 1])
	cond_5 = int(n[i + 1])
	
	state_1 = 1 == 0 #checks if it is the start of the string
	state_2 = cond_1 == cond_4 #checks if next number is equal
	state_3 = cond_1 == cond_2 #checks if next number is adjacent by + 1
	state_4 = cond_1 == cond_3 #checks if next number is adjacent by - 1
	
	if(state_1 or state_2 or state_3 or state_4):
		return n[i]
	else:
		return False

def find_product(n):
	n = 1
	for x in n:
		n += x
	return n

def find_sequence(n):
	adjacent_array = [] #Holds the sequence of adjacent numbers
	product_array = [] #Holds all the product of 13 digits sequences of adjacent numbers

	j = 0
	while j + 1 < len(n):
		if(find_adjacent(n, j)): #Find out if the next number is adjacent
			adjacent_array.append(find_adjacent(n, j)) #The adjacent number
		elif(len(adjacent_array) == 13): #Checks if sequence is of length 13
			product_array.append(find_product(n)) #Appends product of number if length is 13
		else:
			del adjacent_array #Deletes the array if the next number is adjacent and if the array isn't of length 13

print find_sequence('12345678912345689')

