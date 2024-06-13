# Question 1: Implement a function to compute max values in a window of k elements that slides through dataset lst_data

def compute_maxes(lst_data: list, k_window: int) -> list[int]:
    '''Computes the max values of each window of k elements that slides through
    dataset lst_data from left to right, each step is 1 element.
    
    Args:
        lst_data: dataset to be computed
        k_window: a window of k elements
    Returns:

        maxes: list of max values in each window that slides through the dataset from right to left
    '''
    max_values = []

    for i in range(0, len(lst_data) - k_window + 1):
        extracted_values = lst_data[i:k_window + i]
        max_value = max(extracted_values)
        
        max_values.append(max_value)

    return max_values
        

num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
k_window = 3


assert compute_maxes(num_list, 3) == [5, 5, 5, 5, 10, 12, 33, 33]
print('Unit test passed!')