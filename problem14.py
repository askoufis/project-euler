hc = 0
n = 0

def sequence():
    global hc
    hc = 0
    for n in range(1, 1000000):
        chain(n)
    print(n)
    
        

def chain(x):
    global hc
    global n
    t = x
    c = 0
    while t != 1:
        if t % 2 == 1:
            t = t * 3 + 1
            c = c + 1
        elif t % 2 == 0:
            t = t / 2
            c = c + 1

    if c > hc:
        hc = c
        n = x

    
        
         
        
