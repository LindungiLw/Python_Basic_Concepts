def swapFL(lst):
    lst[0], lst[-1] = lst[-1], lst[0]

ingredients = ['flour', 'sugar', 'butter', 'apples']
swapFL(ingredients)
print(ingredients)