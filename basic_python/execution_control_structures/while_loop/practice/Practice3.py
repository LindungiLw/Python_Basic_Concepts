num = int(input("Enter a number (enter 99999 to stop): "))

while num != 99999:
    count = 0
    while count < num:
        print(num)
        count += 1
    num = int(input("Enter a number (enter 99999 to stop): "))
