def factors(n):
    return set(x for tup in ([i, n//i] 
        for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)

#finds factors and outputs a set

amicablePairs = set()               #a set is used to avoid duplicate pairs

for i in range(1,10001):
    total1 = 0
    total2 = 0
    for j in factors(i):
        total1 = total1 + j
        
    total1 = total1 - i             #subtracting i as proper divisors of i does not include themselves
    
    for k in factors(total1):
        total2 = total2 + k

    total2 = total2 - total1        #same as for total1
    
    if (i == total2 and i != total1):
        amicablePairs.add(total1)
        amicablePairs.add(total2)

amicableSum = 0

for i in amicablePairs:
    amicableSum = amicableSum + i

print(amicableSum)
