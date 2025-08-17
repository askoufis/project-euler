f = open('problem13.txt', 'r+')

numbers = f.readlines()

total = 0

for x in range(len(numbers)):
    total = total + int(numbers[x])
print(total)
