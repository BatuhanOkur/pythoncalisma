def recursiveFib(x):
    """
    Girilen sıradaki fibonnaci sayısını bulan recursive fonksiyon.
    """
    if x == 1:
        return 1
    elif x == 2:
        return 1
    
    return recursiveFib(x-1) + recursiveFib(x-2)

print(recursiveFib(10)) 
