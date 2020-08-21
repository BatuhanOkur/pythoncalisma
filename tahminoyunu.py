#Biz 1 ile 100 arasında bir sayı seçiyoruz,bilgisayar tahmin etmeye çalışıyor.Verdiğimiz direktiflere göre tahminleri şekilleniyor.
#Eğer direktifim 1 ise tahminini yükseltecek,-1 ise düşürecek.
import random

sayi = int(input("Bir sayi girin : "))
alt,ust = 1,100
tahmin = (alt+ust)//2
while tahmin != sayi:
    print("Tahminim : ",tahmin)
    direktif = int(input("Direktifiniz nedir? :"))
    if direktif == 1:
        alt = tahmin
        tahmin = (alt+ust)//2
    elif direktif == -1:
        ust = tahmin
        tahmin = (alt+ust)//2
    else:
        print("**HATA**Gecersiz direktif girdiniz!!")
print("Sayiyi buldum : ",tahmin)
