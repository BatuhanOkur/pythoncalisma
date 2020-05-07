def f(x):
    return(3*x**3+2*x**2+5)

a = 0
b = 3
deltax = 0.0001 #Bu değer küçüldükçe bulmamız gereken sonuca daha yakın bir değer buluruz.Dikdörtgen sayısını arttırmış oluyoruz.
integral = 0

n = int((b-a)/deltax) #Düzlemde fonksiyonun altında kalan dikdörtgen sayısını verir. 

for i in range(n):
    integral += deltax*f(a)
    a += deltax

print(integral)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Büyük dikdörtgenler ile yapılmış hali.
#Bu sefer de sonuç bulmam gerekenden fazla çıkıyor ve deltax küçüldükçe fazladan alınan alanlar azalmış oluyor,gerçek değere yaklaşılıyor.
def f(x):
    return(3*x**3+2*x**2+5)

a = 0
b = 3
deltax = 0.05 
integral = 0

n = int((b-a)/deltax)

for i in range(n):
    integral += deltax*f(a+deltax)
    a += deltax

print(integral)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Uzun ve kısa dikdörtgenlerin ortasındaki noktaya göre integral alınıyor ve aynı zamanda yamuk yöntemidir.
#Hassasiyet çok artar ve doğru sonuca çok yakın bir sonuç bulunur.

def f(x):
    return(3*x**3+2*x**2+5)

a = 0
b = 3
deltax = 0.0001
integral = 0

n = int((b-a)/deltax)

for i in range(n):
    integral += deltax*(f(a)+f(a+deltax))/2
    a += deltax

print(integral)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Üstel bir ifade üzerinde deneyelim.
#Normaldeki sonuç 19.08 bizim bulduğumuz sonuç ise 19.48 oluyor.Deltayx'i bir hayli yüksek almamıza rağmen çok yakın bir sonuç bulduk.
#Eğer deltax'i 0.0001 alsaydık çok daha yakın bir sonuç elde edebilirdik.

from math import e
def f(x):
    return(e**x)

a = 0
b = 3
deltax = 0.05
integral = 0

n = int((b-a)/deltax)

for i in range(n):
    integral += deltax*(f(a)+f(a+deltax))/2
    a += deltax

print(integral)

