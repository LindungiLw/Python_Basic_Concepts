days = ('Mo', 'Tu', 'We')
print(days)

days = 'Mo', 'Tu', 'We', 'Th'
print(days)

print('Fr' in days)

week = days + ('Fr', 'Sa', 'Su')
print(week)
print(week[2])
print(len(week))
print(2*week)

days = ('Mo')
print(days)
print(type(days))

t = (3)
print(type(t))


days = ('Mo',)
print(days)
print(type(days))

my_tuple = (11, 3, 15, 7, 9)
my_list = list(my_tuple)
print(my_list)

my_list.sort()
print(my_list)

sorted_tuple = tuple(my_list)
print(sorted_tuple)

list1 = ["Nasi goreng", "Mie goreng", "Sate", "Rendang"]
list2 = list1[:3]

tuple1 = ("soccer", "Football", "Badminton")
list1 = list(tuple1)
print("list1 is", list1)

list1.append("fencing")
list1.sort()
print("list1 is", list1)

tuple2 = tuple(list1)
print("result is", tuple2)