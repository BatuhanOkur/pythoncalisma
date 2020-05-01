girilensayi=int(input("Kacinci fibonacci sayisini bulalim:"))
fib1=1
fib2=1
for i in range(3,girilensayi+1):
    fib=fib1+fib2
    fib1=fib2
    fib2=fib
print(fib)
