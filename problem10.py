import prime

def sumprimesbelow(num):
    x = 1
    y = 0

    while prime.prime(x) < num:
        y += prime.prime(x)

        x += 1

    return y
