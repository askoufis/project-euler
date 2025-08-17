import time

def factors(n):
    return set(x for tup in ([i, n//i]
        for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)

def isAbundant(n):
    fact = factors(n)
    # Remove n from the list of factors
    fact.remove(n)
    return sum(fact) > n

def findAbundBelow(n):
    abund = []

    # Find all abundant numbers below n
    for i in range(2, n+1):
        if isAbundant(i):
            abund.append(i)

    return abund

if __name__ == '__main__':
    limit = 28123
    start = time.time()
    abund = findAbundBelow(limit)

    hasAbundantSum = [0] * (limit+1)

    for i in range(len(abund)):
        for j in range(i, len(abund)):
            if abund[i] + abund[j] <= limit:
                hasAbundantSum[abund[i] + abund[j]] = 1

            else:
                break

    sum = 0

    for i in range(1, 28123+1):
        if not hasAbundantSum[i]:
            sum += i
    print('Sum = ', sum)
    print(time.time() - start)
