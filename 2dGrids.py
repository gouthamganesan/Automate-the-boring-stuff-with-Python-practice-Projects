grid = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I'],
    ['J', 'K', 'M']
]

for x in grid:
    for y in x:
        print(y, end='\t')
    print('\n\n')

print("Transpose")

for y in range(len(grid[0])):
    for x in range(len(grid)):
        print(grid[x][y], end='\t')
    print('\n\n')