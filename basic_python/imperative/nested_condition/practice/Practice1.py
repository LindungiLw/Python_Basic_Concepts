temperature = float(input("Enter the current temperature in Celsius: "))

if temperature >= 35:
    print("Very hot.")
elif temperature >= 28:
    print("Hot.")
elif temperature >= 15:
    print("Warm.")
elif temperature >= 5:
    print("Pleasant.")
else:
    print("Chilly.")
