#!/usr/bin/python3
# -*- coding: utf-8 -*-

# İkinci dereceden bilinmeyen bir fonksiyonun kökünü,rastgele iki x değeri tahmin ederek bulmaya çalışıyoruz.
# Amaç arama yaptığımız aralığı sürekli olarak daraltarak köke yaklaşabildiğimiz en yakın oranda yaklaşabilmek veya kökü tam olarak bulabilmek.

def fonk(x):
    return (x**2-2*x-15)

x1=int(input("Birinci tahmininizi girin:"))
x2=int(input("İkinci tahmininizi girin:"))

if(fonk(x1)*fonk(x2)>0):
    print("Aradığınız değerler arasında kök yok.")
elif(fonk(x1)*fonk(x2)==0):
    print("Köklerden biri, yazdığınız değerlerden biri")
else:
    i=0
    while(i<100):
        xo=(x1+x2)/2
        if(fonk(xo)==0):
            print("kök buldunuz!",xo,i)
            break
        elif(fonk(x1)*fonk(xo)<0):
            x2=xo
        else:
            x1=xo
        print(xo)
        i=i+1
