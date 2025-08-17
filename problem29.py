import time

def setAB(n):
    terms = set()

    for a in range(2, n+1):
        for b in range(2, n+1):
            terms.add(a**b)

    return terms

if __name__ == '__main__':
    start = time.time()

    print(len(setAB(100)))

    print(time.time() - start)