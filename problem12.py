def nu_of_factors1(n):
    result_set = set()
    sqrtn = int(n**0.5)
    for i in range(1,sqrtn+1):
        q, r = n/i, n%i
        if r == 0:
            result_set.add(q)
            result_set.add(i)
    return len(result_set)

for i in range(1, 1000000000):
    n = i * (i + 1) / 2

    if nu_of_factors1(n) > 500:
        print (n)

        break
