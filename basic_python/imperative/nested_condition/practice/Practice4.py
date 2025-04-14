score = int(input("Enter your score: "))
method = input("Enter evaluation method (PF or grade): ")

if method == "PF":
    if score >= 70:
        print("Pass.")
    else:
        print("Fail.")
elif method == "grade":
    if score >= 90:
        print("A.")
    elif score >= 80:
        print("B.")
    elif score >= 70:
        print("C.")
    else:
        print("F.")
else:
    print("Invalid evaluation method.")