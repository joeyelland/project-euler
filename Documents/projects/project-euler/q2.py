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
    else:
        i += 1
        k += 1

print total
