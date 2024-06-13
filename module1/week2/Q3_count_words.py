# Question 3: Count the number of occurrences of words from P1_data.txt file


def count_words(filepath: str) -> dict:
    '''Count the number of occurrences of words from file with filepath
    
    Args:
        filepath: path to the file containing texts

    Returns:
        word_dict: dictionary containing words and their number of occurrences
    '''
    # Initalize a dictionary to store the occurrences
    word_dict = {}

    # Read the file
    with open('P1_data.txt', 'r') as file:
        contents = file.readlines()

    # Processing data
    for line in contents:
        words = line.strip().split(' ')
        
        for word in words:
            word = word.lower()
            
            word_dict[word] = word_dict.get(word, 0) + 1

    word_dict = dict(sorted(word_dict.items()))
    return word_dict

print(count_words('P1_data.txt'))
