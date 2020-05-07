def nCr(n,r):
    from math import factorial
    return(factorial(n)/(factorial(r)*factorial(n-r)))

def f(x):
    return(x**3+2*x+8)

x0 = 1
h = 0.0001
n = 2
xprime = 0

for k in range(0,n+1):
    xprime += (-1)**(k+n)*nCr(n, k)*f(x0+k*h)
    
print(xprime*(1/(h**n)))
