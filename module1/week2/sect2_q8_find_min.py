# Question 8:

def find_min(lst_data):

    if not isinstance(lst_data, list):
        return "Data type not supported"
    
    if len(lst_data) == 0:
        return 'Empty list'
    
    min_value = lst_data[0]

    for element in lst_data[1:]:
        if element < min:
            min_value = element
    return min_value

my_list = [1, 22, 93, -100]
assert find_min(my_list) == -100
assert find_min('a') == 'Data type not supported'
assert find_min([]) == 'Empty list'

my_list = [1, 2, 3, -1]
print(find_min(my_list))

# Question 8: Answer C