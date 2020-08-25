#https://projecteuler.net/problem=3
import math
def smallestPrimeFactor(n):
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n

n = 600851475143
while True:
    f = smallestPrimeFactor(n)
    if f < n:
        n //= f
    else:
        break
print(n)

