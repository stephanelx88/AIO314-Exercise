# Question 5:

def check_the_number(N):
    '''
    Checks the number N is in the list or not. Returns a string "True"
    if it is, "False" otherwise.

    Args:
        N: number to check
    
    Returns:
        result: string "True" or "False"
    '''
    
    list_of_numbers = []
    
    result = ""

    for i in range(1, 5):
        list_of_numbers.append(i)

    if N in list_of_numbers:
        result = "True"
    if N not in list_of_numbers:
        result = "False"
    
    return result



N = 7

assert check_the_number(N) == "False"
N = 2
results = check_the_number(N)
print(results)

# Question 5: Answer A