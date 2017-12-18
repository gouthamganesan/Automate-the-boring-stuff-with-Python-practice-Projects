tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]

max_length = [0] * len(tableData)

for y in tableData:
    max_value = 0
    for x in y:
        if len(x) > max_value:
            max_value = len(x)
    max_length[tableData.index(y)] = max_value

print(max_length)

for y in range(len(tableData[0])):
    for x in range(len(tableData)):
        max_value = max_length[x]
        string = tableData[x][y]
        print(string.rjust(max_value), end=' ')
    print()
