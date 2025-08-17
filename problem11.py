f = open("problem11.txt", "r")

numbers = f.readlines()

line = 0
x = 0
y = 2
highest = 0
product = 0

for i in range(400):
    if x <= 48:
        product = int(numbers[line][x:y]) * int(numbers[line][x+3:y+3]) * int(numbers[line][x+6:y+6]) * int(numbers[line][x+9:y+9])
        if  product > highest:
            highest = product

    if x <= 48 and line < 17:
        product = int(numbers[line][x:y]) * int(numbers[line+1][x+3:y+3]) * int(numbers[line+2][x+6:y+6]) * int(numbers[line+3][x+9:y+9])
        if product > highest:
            highest = product

    if line < 17:
        product = int(numbers[line][x:y]) * int(numbers[line+1][x:y]) * int(numbers[line+2][x:y]) * int(numbers[line+3][x:y])
        if product > highest:
            highest = product
            
    if line < 17 and x > 12:
        product = int(numbers[line][x:y]) * int(numbers[line+1][x-3:y-3]) * int(numbers[line+2][x-6:y-6]) * int(numbers[line+3][x-9:y-9])
        if product > highest:
            highest = product

    x = x + 3
    y = y + 3

    if i+1 > 0 and (i+1) % 20 == 0:
        line = line + 1
        x = 0
        y = 2

    
    
print(str(i) + " " + str(highest))
    



