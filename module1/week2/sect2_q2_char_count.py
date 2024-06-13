# Question 2:

def character_count(word):
    character_statistic = {}

    for char in word:
        character_statistic[char] = character_statistic.get(char, 0) + 1


    return character_statistic


assert character_count('Baby') == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
print(character_count('smiles'))

# Question 2: Answer A