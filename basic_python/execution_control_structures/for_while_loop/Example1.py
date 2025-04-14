string = "HelloWorld"
word = ""
count = 1

for s in string:
    if count % 2 == 0:
        word += s
    count += 1

print(word)