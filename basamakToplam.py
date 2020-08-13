#Girilen sayının basamaklarındaki sayıların toplamını çıktı olarak verir.

sayi = input("Sayi girin:")
sayiLen = len(sayi)
i = 1
toplam = int(sayi[0])
while i < sayiLen:
    toplam += int(sayi[i])
    i += 1
print("Girilen sayı : ",sayi)
print("Basamakları toplamı : ",toplam)
