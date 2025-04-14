body_temp = float(input("Enter your body temperature in Celsius: "))

if body_temp >= 37.5:
    print("High fever.")
elif body_temp >= 35.5:
    print("Normal temperature.")
else:
    if body_temp >= 34:
        print("Low temperature.")
    else:
        print("Very low temperature.")
