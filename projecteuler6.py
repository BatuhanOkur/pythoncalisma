#https://projecteuler.net/problem=6
sumOfSquares = 0
s = 0
for i in range(1,101):
    sumOfSquares += i**2
    s += i
dif = (s**2) - sumOfSquares
print(dif)
