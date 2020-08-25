#https://projecteuler.net/problem=1
toplam = 0
for n in range(1000):
    if(n % 3 == 0 or n % 5 == 0):
        toplam += n
print(toplam)
