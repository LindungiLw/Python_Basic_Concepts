age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
elif age == 18 or age < 60:
    print("You are in middle age.")
else:
    print("You are a senior citizen.")