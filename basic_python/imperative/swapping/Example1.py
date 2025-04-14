from basic_python.data_type.list_tuple.List import fruits


def exchange(listN, i, j):
    temp = listN[i]
    listN[i] = listN[j]
    listN[j] = temp

nums = [1, 3, 5, 7, 9, 11]
fruits = ['apple', 'banana', 'mango', 'pineapple', 'melon']

print("*" * 50)
print(nums)
print(fruits)

exchange(nums, 0, 1)
exchange(fruits, 0, 1)
print("exchange index 0, 1 = ", nums)
print(fruits)