#https://projecteuler.net/problem=2
fib = 0
fib1 = 1
fib2 = 2
while fib1 < 4000000:
    if fib1 % 2 == 0:
        fib += fib1
    fib1,fib2 = fib2,fib1+fib2
print(fib)

