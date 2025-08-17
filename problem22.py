f = open("problem22.txt", "r")

names = f.read()
names = names[1:]
names = names[:-1]
names = names.split('","')
names.sort()

value_letters = {}
start = ord("A")
for i in range(0, 26):
    value_letters[chr(start+i)] = i + 1

total = 0

for i in range(1, len(names)+1):
    name = names[i-1]
    sum_letters = 0
    for letter in name:
        sum_letters += value_letters[letter]*i
    total += sum_letters

print(total)
