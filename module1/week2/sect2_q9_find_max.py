# Question 9:

def find_max(lst_data):

    if not isinstance(lst_data, list):
        return "Data type not supported"
    
    if len(lst_data) == 0:
        return 'Empty list'
    
    max_value = lst_data[0]

    for element in lst_data[1:]:
        if element > max_value:
            max_value = element
    return max_value

my_list = [1001, 9, 100, 0]
assert find_max(my_list) == 1001
assert find_max('a') == 'Data type not supported'
assert find_max([]) == 'Empty list'

my_list = [1, 9, 9, 0]
print(find_max(my_list))

# Question 9: Answer D