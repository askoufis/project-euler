def isprime(n):   
    if n < 2:
        return False

    if n == 2:
        return True

    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
        
    return True

def pfactors(n):
    pfactors = []

    check = 2

    rootn = int(n ** 0.5)

    while check < rootn:
        if n % check == 0 and isprime(check):
            pfactors.append(check)
        check += 1

    if rootn == check and isprime(check):
        pfactors.append(check)

        pfactors.sort()

    return pfactors
