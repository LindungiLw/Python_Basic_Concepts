sp = {'one': 'satu', 'two': 'dua', 'three': 'tiga'}
print(sp.get('two'))
print(sp['one'])
print(sp.keys())

animal = {'a': 'ant', 'b': 'lion', 'c': 'tiger'}
animal1 = {'g': 'squirrel', 'd': 'snake', 'f': 'dog'}
animal.update(animal1)
print(animal)

t = [('a', 0), ('c', 2), ('b', 1)]
result = dict(t)
print(result)