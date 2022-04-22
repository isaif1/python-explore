#take a certain number and raise it to certain power

print(2**3)

#2D lists and nested loop

grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

for row in grid:
    for col in row:
        print(col)