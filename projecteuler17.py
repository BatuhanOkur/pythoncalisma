#https://projecteuler.net/problem=17
floorOne = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
floorTen = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
def convertToString(n):
    if 0 <= n < 20:
        return floorOne[n]
    elif 20 <= n < 100:
        return floorTen[n // 10] + (floorOne[n % 10] if (n % 10 != 0) else "")
    elif 100 <= n < 1000:
        return floorOne[n // 100] + "hundred" + (("and" + convertToString(n % 100)) if (n % 100 != 0) else "")
    elif 1000 <= n < 1000000:
        return convertToString(n // 1000) + "thousand" + (convertToString(n % 1000) if (n % 1000 != 0) else "")

ans = sum(len(convertToString(i)) for i in range(1, 1001))
print(ans)
