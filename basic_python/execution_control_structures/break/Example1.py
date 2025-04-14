count = 0

for i in range(5):
    for j in range(3):
        if (i + j) % 5 != 0:
            count += 1
            print("i + j = ", i+j, "and count = ", count)
        else:
            break

print("i + j = ", i + j, "last count: ", count)