attempts = 0
password = ""

while password != '1111' and attempts < 5:
    password = input("Enter password: ")
    attempts += 1

print("Program terminated…")