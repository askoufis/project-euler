def product5(num):
    l = []

    k = []
    
    x = str(num)
    
    for i in x:
        l.append(i)

    j = len(str(num))

    s = 0

    while s < j - 4:
        a = int(l[s]) * int(l[s + 1]) * int(l[s + 2]) * int(l[s + 3]) * int(l[s + 4])
        k.append(a)
        s += 1

    k.sort()

    return k
