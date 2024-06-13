# Question 2: Implement a function to count characters in a string

def count_chars(string: str) -> dict:
    '''Count the occurrences of characters in a string
    
    Args:
        string: a string to count characters

    Returns:
        char_dict: a dictionary conataining characters and their ocurrences
                    in the string
    '''
    char_dict = {}

    for char in string:
        char_dict[char] = char_dict.get(char, 0) + 1

    return char_dict

print(count_chars('Happiness'))
print(count_chars('smiles'))