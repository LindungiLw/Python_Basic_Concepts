str1 = 'hi'

def foo():
    global str1
    str1 = "hello"
    print(str1)

foo()
print(str1)