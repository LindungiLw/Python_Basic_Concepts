name = input("Enter your name: ")
age = input("Enter your age: ")
address = input("Enter your address: ")
major = input("Enter your major: ")

info = [('Name', name), ('Age', age), ('Address', address), ('Major', major)]
print('Info =', dict(info))