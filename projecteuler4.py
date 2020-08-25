#https://projecteuler.net/problem=4
product = []
for i in range(100,1000):
    for j in range(100,1000):
        if str(i*j) == str(i*j)[::-1]:
            product.append(i*j)
print(max(product))
