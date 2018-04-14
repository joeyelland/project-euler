#Each new term in the Fibonacci sequence is generated by adding the previous two terms.
#By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#!/usr/bin/python
i = 0 #counter1
k = 1 #counter2
next_num = 0
total = 2 #result
fibo_arr = [1, 2]

while (next_num <= 4000000):
    next_num = fibo_arr[i] + fibo_arr[k]
    fibo_arr.append(next_num)
    if (next_num % 2 == 0):
        total += next_num
    i += 1
    k += 1

print total
