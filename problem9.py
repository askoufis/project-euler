def pythagorean_triplet():
    for a in range(1, 501):
        for b in range(1, 501):
            c = 1000 - a - b
            if (a*a + b*b == c*c):
                print (a, b, c)
                
                return a*b*c
