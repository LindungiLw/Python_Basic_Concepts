fruits = ['apple’, ’banana', 'mango', 'pineapple']
print (fruits[2])
numbers = [1, 3,2, 5,7,9, 34,34, 54,266]
print (numbers)

a = list(range(10))
print(a)
print(a[2] )
print(a [5] )
print(a[0]+a[3])

animal = ['cat', 'dog', 'sheep', 'cow']

print(animal[0])
print(animal[1])
print(animal[2])
print(animal[3])

birthday = '9/6/2007'
print(birthday.split('/'))

splitme = 'a/b//c/d///e'
print(splitme.split('/'))

splitme = 'a/b//c/d///e'

print(splitme.split('/', 2))
print("\nAdditional Splitting Examples:")
print("a.b.c.d".split('.'))
print("hello world".split())
print("one  two   three".split())

marxes = ['Groucho', 'Chico', 'Harpo']

print(marxes[0])
print(marxes[1])
print(marxes[2])
print(marxes[-1])
print(marxes[-2])
print(marxes[-3])

print("\nList Length:", len(marxes))
print("First Two:", marxes[:2])

marxes = ['Groucho', 'Chico', 'Harpo']

print(marxes[0:2])
print(marxes[::2])
print(marxes[::-2])
print(marxes[::-1])

marxes = ['Groucho', 'Chico', 'Harpo']
marxes.append('Zeppo')
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.extend(others)
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes += others
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.append(others)
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.insert(3, 'Gummo')
print(marxes)

marxes = ['$roucho', 'Chico', 'Harpo', '6ummo', 'Zeppo', 'Karl']
del marxes[-1]
print(marxes)

print(marxes[2])
del marxes[2]
print(marxes)

marxes.remove('6ummo')
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.pop()
print(marxes)

marxes.pop(1)
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']

print(marxes.index('Chico'))
print('Groucho' in marxes)
print('Bob' in marxes)
print(marxes.count('Harpo'))
print(marxes.count('Bob'))

numbers = [2, 1, 4.0, 3]
numbers.sort()
print(numbers)

marxes = ['Groucho', 'Chico', 'Harpo']
print(','.join(marxes))

friends = ['Ray', 'Najib', 'Grace', 'Diaz', 'Julior']
separator = '*'
joined = separator.join(friends)
print(joined)

sorted_friends = sorted(friends)
print(sorted_friends)
print(friends)
friends.sort()
print(friends)