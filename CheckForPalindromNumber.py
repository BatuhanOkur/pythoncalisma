sayi=int(input("Hangi sayiyi test etmek istersiniz:"))
temp=sayi
top=0
while(sayi>0):
    mod = sayi % 10
    sayi = (sayi - mod)/10
    top = top * 10 + mod 
if(temp == top):
    print("Girdiginiz sayi palindrom.")
else:
    print("Girdiginiz sayi palindrom degil.")
    
# ya da pythonun kolayliklarindan faydalanip asagidaki yontemi kullanabiliriz.    
def ispalindrome(n):
    if str(n) == str(n)[::-1]:
        return "1"
    else:
        return "0"
