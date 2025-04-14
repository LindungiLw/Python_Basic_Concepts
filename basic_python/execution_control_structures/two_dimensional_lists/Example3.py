a = [[10, 20], [30, 40], [50, 60]]

for i in range(2):
    for j in range(3):
        if j == 0:
            a[j][i] = a[j][i] * 10
        print(a[j][i])