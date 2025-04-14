def fun(count):
    global a
    a = 5
    count += a
    return count

count = 0
print("result :", fun(count))

print(a)