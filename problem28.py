import math

def spiral(x):
    total = 1
    n = 1
    for i in range(1, math.ceil(x/2)):
        for a in range(4):
            n = n + 2*i
            total = total + n

    print(total)
