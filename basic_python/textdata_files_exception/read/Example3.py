def numLines(filename):
    infile = open(filename, "r")
    lineList = infile.readlines()
    infile.close()

    print(lineList)
    return len(lineList)

num = numLines("numbers.txt")
print(num)