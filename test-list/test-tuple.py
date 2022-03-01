number_tuple = (1, 'test', [1, 0.2])
print(number_tuple)
temp_list = list(number_tuple)
print(temp_list)
temp_list[1] = 'testtest'
print(temp_list)
number_tuple_2 = tuple(temp_list)
print(number_tuple_2)