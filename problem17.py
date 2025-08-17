num = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8, 20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6, 100: 7, 1000:8}

totalLetterCount = 0

def count(i):
    global totalLetterCount
    letterCount = 0
    if (i > 9 and i < 20):                                      #checking from 11 to 19
        letterCount = letterCount + num[i]                      #adding letters
        
    elif (int(str(i)[-2:]) > 9 and int(str(i)[-2:]) < 20 and len(str(i)) == 3):
                                                                #checking 11 to 19 in 3 digit numbers
        letterCount = letterCount + num[int(str(i)[-2:])]       #adding letters for 11 to 19 part
        letterCount = letterCount + num[int(str(i)[0])]         #letters for the digit of the hundreds
        letterCount = letterCount + 3                           #letters for 'and'
        letterCount = letterCount + num[100]                    #letters for hundred
        
    elif (len(str(i)) == 1):                                    #1 digit numbers
        letterCount = letterCount + num[i]
        
    elif (len(str(i)) == 2):                                    #2 digit numbers
        letterCount = letterCount + num[int(str(i)[1])]         #units
        letterCount = letterCount + num[int(str(i)[0]) * 10]    #tens

    elif (len(str(i)) == 3):                                    #3 digit numbers
        letterCount = letterCount + num[int(str(i)[2])]         #units
        letterCount = letterCount + num[int(str(i)[1]) * 10]    #tens
        if (int(str(i)[1]) != 0 or int(str(i)[2]) != 0):        #if the second and third digits are non-zero
            letterCount = letterCount + 3                       #letters for 'and'             
        letterCount = letterCount + num[int(str(i)[0])]         #hundreds
        letterCount = letterCount + num[100]                    #letters for hundred

    elif (len(str(i)) == 4):
        letterCount = letterCount + num[1000]                   #thousand
        letterCount = letterCount + 3
        
    totalLetterCount = totalLetterCount + letterCount
    
    return letterCount

for a in range(1, 1001):
    count(a)

print(totalLetterCount)
