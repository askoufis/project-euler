x = 0
answer = 0

while x < 1000:    
    if x % 3 == 0 or x % 5 == 0:
        answer = answer + x
        x = x + 1
    else:
        x = x + 1
    
print(answer)
