num1 = {1,2,3,4,5}
num2 = {4,5,6,7,8}
num3 = {1,4}

print(num1 & num2)
print(num1.intersection(num2))
print(num1 & num2 & num3)

print(num1 | num2)
print(num1.union(num2))
print(num1 | num2 | num3)

print(num1 - num2)
print(num1.difference(num2))

print(num1 ^ num3)
print(num1.symmetric_difference(num3))

print(num1 <= num1)
print(num1.issubset(num1))

print(num1 < num1)

print(num1 >= num3)
print(num1.issuperset(num3))

print(num1 > num3)