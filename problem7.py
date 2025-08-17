def prime(num):
    for x in range (2, num):
        if num % x == 0:
            return 1
            break

c = 0

for val in range(2, 110000):
    is_prime = prime(val)
    if is_prime != 1:
        c = c + 1
        if c == 10001:
            print(val)
            break


            

