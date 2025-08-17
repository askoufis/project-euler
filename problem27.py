import time

def quadratic(n, a, b):
    return n*n + a*n + b

def isPrime(n):
    k = 3
    flag = True

    if (n == 2):
        flag = True

    elif (n % 2 == 0 or n == 1):
        flag = False

    else:
        while (k*k <= n):
            if (n % k == 0):
                flag = False
                break
            k += 1


    return flag

if __name__ == '__main__':
    start = time.time()

    longestPrimes = 0
    longestA = 0
    longestB = 0

    for a in range(-999, 1000):
        for b in range(-999, 1000):
            n = 0

            consecutive = True

            while consecutive:
                val = quadratic(n, a, b)

                if val <= 0:
                    consecutive = False

                elif not isPrime(val):
                    consecutive = False

                else:
                    n += 1

            if n > longestPrimes:
                print('New best at ' + str(n) + ' primes!')
                longestPrimes = n
                longestA = a
                longestB = b

    print('Product = ', str(longestA*longestB))
    print(time.time() - start)
