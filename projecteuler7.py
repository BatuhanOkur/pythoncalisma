#https://projecteuler.net/problem=7
from functions import isprime

number,counter = 1,0
while counter< 10001:
    number += 1
    if isprime(number) == 1:
        counter += 1

print(number)
