my_dict = {'name': 'Anton', 'birthday':2001, 'phone':123456789, 'city': 'Moscow'}
print(my_dict)
print(my_dict.get('name'))
print(my_dict.get('age'))
my_dict.update({'age': 100, 'year': 2024})
a = my_dict.pop('name')
print(a)
print(my_dict)
my_set = {1, 1.1, 'street', 'street', (777), (777)}
print(my_set)
my_set.update({10, 10, 'name', 'name'})
my_set.discard((777))
print(my_set)