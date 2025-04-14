def arithmetic(numbers):
    if len(numbers) <= 2:
        return True

    diff = numbers[1] - numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i - 1] != diff:
            return False

    return True

print(arithmetic([3, 6, 9, 12, 15]))
print(arithmetic([3, 6, 9, 11, 14]))
print(arithmetic([3]))