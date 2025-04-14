multiplication_table = []

for i in range(2, 17):
    row = []
    for j in range(2, 17):
        row.append(i * j)
    multiplication_table.append(row)

for row in multiplication_table:
    print(row)
