t = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 7]]

for row in t:
    print(row)

def print2D(t):
    for row in t:
        for item in row:
            print(item, end=' ')
        print()

def incr2D(t):
    nrows = len(t)
    ncols = len(t[0])

    for i in range(nrows):
        for j in range(ncols):
            t[i][j] += 1

print2D(t)
incr2D(t)
print2D(t)