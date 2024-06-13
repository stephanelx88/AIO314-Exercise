# Question 3:

def count_word(file_path):

    counter = {}

    # Read the file
    with open(file_path, 'r') as f:
        contents = f.readlines()

    # Loop through the lines
    for line in contents:
        words = line.strip().split(' ')

        # Loop through each word
        for word in words:
            word = word.lower()

            counter[word] = counter.get(word, 0) + 1

    return counter
file_path = 'P1_data.txt'
result = count_word(file_path)
assert result['who'] == 3
print(result['man'])

# Question 3: Answer C