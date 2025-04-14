s = [["Smith", 90, 75], ["Putri", 89, 95], ["Gloria", 76, 85]]
print(s)

for i in range(len(s)):
    print(s[i][0])
    sum = 0
    for j in range(1, len(s[i])):
        sum = sum + s[i][j]

    print("sum =", sum, "average =", sum/j)
    