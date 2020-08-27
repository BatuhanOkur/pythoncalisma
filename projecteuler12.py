#https://projecteuler.net/problem=12
from functions import divisors
number = 28
for i in range(8,1000000):
    number += i
    if(len(divisors(number)) > 500):
        print(number)
        break
