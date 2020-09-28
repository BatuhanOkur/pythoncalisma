#https://projecteuler.net/problem=16
n = 32768
for i in range(16,1001):
    n += n
s = str(n)
bt = 0
for n in s:
    bt += int(n)
print(bt)

