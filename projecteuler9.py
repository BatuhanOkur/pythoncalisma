#https://projecteuler.net/problem=9
for a in range(1,400):
    for b in range(a+1,400):
        c = 1000-a-b
        if a**2 + b**2 == c**2:
            specialProduct = a*b*c
print(specialProduct)
