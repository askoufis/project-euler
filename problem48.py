def exp(n):
    global answer
    answer = 0
    while n > 0:
        a = n**n
        answer = answer + a
        n = n - 1
    print(answer)
        
