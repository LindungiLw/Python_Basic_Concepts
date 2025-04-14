def strFunction(str1, str2):
    r1 = False
    r2 =  False

    if len(str1) > len(str2):
        r1 = True
    if str1 > str2:
        r2 = True

    return r1, r2

str1 = 'lemon'
str2 = 'cherry'
result1, result2 = strFunction(str1, str2)

print("The length of list str1 larger than str2",result1)
