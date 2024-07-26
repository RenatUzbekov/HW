immutable_var = 1, 1.1, 'python', True
print(immutable_var)
immutable_var = [1, 1.1,'python'], True
immutable_var[0][2] = 3
print(immutable_var)
mutable_list = ['Moscow', 'Murmansk', 'Kazan']
mutable_list[0] = 'Ufa'
print(mutable_list)