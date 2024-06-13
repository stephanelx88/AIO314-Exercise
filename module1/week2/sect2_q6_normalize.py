# Question 6: 

def normalize(data, max_val, min_val):
    """
    This function cleans up data by replacing min for values less than min
    and max for values greater than max. Otherwise, keep the data as is.

    Args:
        data: dataset to be cleaned up
        max: max value
        min: min value

    Args:
        result: the returned cleaned data
    """
    result = []

    for i in data:
        if i < min_val:
            result.append(min_val)
        elif i > max_val:
            result.append(max_val)
        else:
            result.append(i)
    return result

my_list = [5, 2, 4, 0, 1]
max_val = 1
min_val = 0
assert normalize(max_val=max_val, min_val=min_val, data=my_list) == [1, 1, 1, 0, 1]
print('passed')
my_list = [10, 2, 5, 0, 1]
max_val = 2
min_val = 1
print(normalize(max_val=max_val, min_val=min_val, data=my_list))

# Question 6: Answer C