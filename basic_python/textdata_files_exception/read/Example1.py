def numChars(filename):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()

    return len(content)

num = numChars('n.txt')
print(num)