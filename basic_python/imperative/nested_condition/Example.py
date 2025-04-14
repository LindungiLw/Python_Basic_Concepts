user = ['Nicho', 'David', 'Jonathan']

user_id = input("Username: ")

if user_id in user:
    pw = input("Password: ")

    if pw == '1234':
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("User not found")