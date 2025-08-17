def fibE(n):            #prints all even fibbonaci numbers
                        #up to n and then adds them
    answer = 0
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
        if b % 2 == 0:
            print(b)
            answer = answer + b
        else:
            print("Odd")

    print(answer)

        
    
