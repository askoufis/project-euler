import time
import numpy

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

def longestRecurringDecimal(l):
    longestLength = 0
    longestValue = 0

    for i in l:
        k = 1

        while (10**k - 1) % i != 0:
            k = k + 1

        if k > longestLength:
            longestLength = k
            longestValue = i

    return longestValue


if __name__ == '__main__':
    start = time.time()

    primes = primesfrom2to(1000)
    print(longestRecurringDecimal(primes))


    print(time.time() - start)