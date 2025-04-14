def sorted(lst):
    for i in range(0, len(lst) - 1):
        if lst[i] > lst[i+1]:
            return False
    return True

list_1 = ['a', 'b', 'c', 'd', 'e']
list_2 = [2, 4, 5, 3, 1]

print(sorted(list_1))
print(sorted(list_2))