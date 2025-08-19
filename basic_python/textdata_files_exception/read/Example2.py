def numWords(filename):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()

    wordList = content.split()
    print(wordList)
    return len(wordList)

num = numWords('numbers.txt')
print(num)