def SumDigits(n):
    numList = list(str(n))
    total = sum(int(c) for c in numList)
    print(total)
