# Question 10:

def is_included(integers, number=1):

    return any([num == number for num in integers])

my_list = [1, 3, 9, 4]
assert is_included(my_list, -1) == False

my_list = [1, 2, 3, 4]
print(is_included(my_list, 2))

# Question 10: Answer C