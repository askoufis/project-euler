import time

def rev(num): #function to reverse a number
    rev = [c * 1 for c in str(num)] #converts num into a list with each digit as a different object
    digits = len(rev) - 1 #finds the number of digits by finding the length of the list, then subtracts 1 becuase the indexing starts at 0
    x = 0 #assigning variable for later
    while digits >= 0:
        if digits >= 0:
            c = int(rev[digits]) #assigns c the value of the last digit (the digits variable) which is converted to an integer
            x = x + c *(10 ** digits) #assigns x to itself plus c times 10 to the power of digits
            digits -= 1 #decrements digits by 1 so the next digit is multiplied by one less 10th power
    global z
    z = x
    


def pal(num):
    c = num
    x = 0
    if c > 100:
        while c > 98:
            rev((num * c))
            if num == 99:
                print(x)
                break
            elif c == 99:
                c = num - 1
                num -= 1
            elif z == num * c and z > x:
                x = z
                c -= 1
            else:
                c -= 1
                

