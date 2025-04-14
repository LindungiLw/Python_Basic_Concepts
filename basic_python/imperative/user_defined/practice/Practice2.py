def noVowel(s):
    for i in s:
        if i in "aeiouAEIOU":
            return False
    return True

print(noVowel(input("Enter a string: ")))
print(noVowel(input("Enter a string: ")))
print(noVowel(input("Enter a string: ")))