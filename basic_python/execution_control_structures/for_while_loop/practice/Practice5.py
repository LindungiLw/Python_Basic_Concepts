name = "Rahma Lindungi Laowo"

for letter in name:
    if letter != ' ':
        print(letter)

count = 0
for letter in name:
    if letter != ' ':
        count += 1

print("Total characters (excluding spaces):", count)