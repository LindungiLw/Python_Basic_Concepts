a = 0
for i in range(10):
    a = a + 1
for j in range(10):
    a = a + 1

print(a)



a = 0
for i in range(10):
    a = a + 1
    for j in range(10):
        a = a + 1

print(a)

a = 0
for i in range(2, 10):
    a = a + i
    for j in range(10, 1, -2):
        a = a + j

print(a)