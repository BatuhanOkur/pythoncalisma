# " a**2*x + b*x + c " şeklindeki bir ikinci derece denklemin köklerinin var olup olmadığını inceleyen,var ise kökleri ile çıktı olarak döndüren fonksiyon.

def ikinciDerecedenDenklemKontrol(a,b,c):
    delta = b**2-4*a*c
    if delta > 0:
        x1 = (-b+delta**(1/2))/(2*a)
        x2 = (-b-delta**(1/2))/(2*a)
        print("İki adet reel kök vardır.")
        print("Birinci : ",x1)
        print("İkinci : ",x2)
    elif delta == 0:
        x1 = -b/(2*a)
        print("İki adet çakışık reel kök vardır.")
        print("Kök : ",x1)
    elif delta < 0:
        print("Reel kök yok.")

print(ikinciDerecedenDenklemKontrol(1,-2,-6)) 

"""
Çıktı : 
İki adet reel kök vardır.
Birinci :  3.6457513110645907
İkinci :  -1.6457513110645907
"""
