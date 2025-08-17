with open('problem18.txt') as f:
    values = []
    for line in f:
        line = line.split() # to deal with blank 
        if line:            # lines (ie skip them)
            line = [int(i) for i in line]
            values.append(line)
        
row = len(values) - 2       # we want to start at the row second from the bottom

for i in range(row, -1, -1):
    for j in range(0, len(values[i])):
        values[i][j] = values[i][j] + max(values[i+1][j], values[i+1][j+1])

print(values[0][0])
