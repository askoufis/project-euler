def fiblen(n):
    a = 0
    b = 1
    c = 1
    x = 0
    while c > 0:
        if len(str(c)) == n:
            x = x + 1
            print('The', str(x) + 'th', 'Fibonnaci number, or', str(c) + ',', 'is the first Fibonnaci number with', n, 'digits.')
            c = 0
        else:
            c = a + b
            a = b
            b = c
            x = x + 1
