x = int(input("Enter a number: "))

if x > 100:
    print("Cannot process this number.")
elif x >= 80:
    print("Your grade is A.")
elif x >= 70:
    print("Your grade is B.")
elif x >= 60:
    print("Your grade is C.")
else:
    print("Your grade is D.")