def SumDigits(n):
    numList = list(str(n))
    total = sum(int(c) for c in numList)
    print(total)

def fact(x): return (1 if x==0 else x * fact(x-1))

def SumFactDigits(n):
    SumDigits(fact(n))
