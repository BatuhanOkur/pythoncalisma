#bilgisayar ile taş kağıt makas oynanıyor
#10 tur oynanıyor,kazanan 10 puan alıyor.
import random
ihtimaller = ["tas","kagit","makas"]
oyuncular =["Siz","Bilgisayar"]
bilgisayar,oyuncu = 0,0
for i in range(10):
    secim = int(input("Tas secmek icin 0,kagit icin 1,makas icin 2 giriniz : "))
    kullanici = ihtimaller[secim]
    rand = random.randint(0,2)
    bilgisayarsecim = ihtimaller[rand] 
    if(secim != rand):
        if (secim-rand) == 1:
            print("\nSiz : ",kullanici)
            print("\nBilgisayar : ",bilgisayarsecim)
            print("\nRaundu Kazanan : ",oyuncular[0])
            print("\n---------------------------------")
            oyuncu += 10
        elif (rand-secim) == 1:
            print("\nSiz : ",kullanici)
            print("\nBilgisayar : ",bilgisayarsecim)
            print("\nRaundu Kazanan : ",oyuncular[1])
            print("\n---------------------------------")
            bilgisayar += 10
        elif (secim-rand) == 2:
            print("\nSiz : ",kullanici)
            print("\nBilgisayar : ",bilgisayarsecim)
            print("\nRaundu Kazanan : ",oyuncular[1])
            print("\n---------------------------------")
            bilgisayar += 10
        else:
            print("\nSiz : ",kullanici)
            print("\nBilgisayar : ",bilgisayarsecim)
            print("\nRaundu Kazanan : ",oyuncular[0])
            print("\n---------------------------------")
            oyuncu += 10
    else:
        print("\nSiz : ",kullanici)
        print("\nBilgisayar : ",bilgisayarsecim)
        print("İki taraf da aynı hamleyi yaptıgı icin kazanan olmadı.")

if (oyuncu != bilgisayar):
    if(oyuncu > bilgisayar):
        print("\n\nOYUN BİTTİ!!")
        print("\nTebrikler siz kazandınız!!")
        print("\nPuanınız : ",oyuncu)
        print("\nRakibinizin puanı : ",bilgisayar)
    else:
        print("\n\nOYUN BİTTİ!!")
        print("\nMaalesef kaybettiniz.")
        print("\nPuanınız : ",oyuncu)
        print("\nRakibinizin puanı : ",bilgisayar)
else:
    print("Berabere bitti,durum 50'ye 50.")
