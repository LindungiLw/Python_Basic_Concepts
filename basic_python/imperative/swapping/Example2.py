def exchange(listN, i, j):
    listN[i], listN[j] = listN[j], listN[i]

nums = [1, 3, 5, 7, 9, 11]
fruits = ['apple', 'banana', 'mango', 'pineapple', 'melon']

print("*" * 50)
print(nums)
print(fruits)

exchange(nums, 0, 1)
exchange(fruits, 0, 1)
print("exchange index 0, 1 = ", nums)
print(fruits)