count = int(input("Enter the number of integers: "))

while count <= 0:
    count = int(input("Please enter a positive number: "))

i = 0
total = 0

while i < count:
    num = int(input(f"Enter integer #{i+1}: "))
    total += num
    i += 1

average = total / count
print("The average is:", average)
