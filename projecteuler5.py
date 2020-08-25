#https://projecteuler.net/problem=5
#i = 2
#number = 2520
#while i != 21:
#    if number % i == 0:
#        i += 1
#    else:
#        number += 1
#        i = 2
#print(number)
#Yukarıda yazdıgım kod ilk aklıma gelen algoritmaydı fakat baya bir uzun surdugunden dolayı bitmesini bile beklemedim.
#Teoride dogru fakat pratikte kullanıssız bir kod.
import math
number = 1
for i in range(1,21):
    number *= i // math.gcd(i,number)
print(number)
#Burada 1 den 20 ye kadar olan tum sayilari carparken fazlalık olan bolenleri bolerek cikartiyorum.
#Ornek 3'e ve 2'ye ayni anda bolunebilen bir sayiya 6 carpanini eklemem gereksiz olur ve en kucugunu bulmami engeller.
