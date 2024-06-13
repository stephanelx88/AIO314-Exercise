def levenshtein(word1: str, word2:str) -> int:
    '''Compute Levenshtein distance between two words
    
    Args:
        word1: the first word
        word2: the second word

    Returns:
        leven_distance: Levenshtein distance between two words
    '''

    # Initial matrix to store costs
    n_row = len(word2) + 1 
    n_col = len(word1) + 1
    
    matrix = [[0 for _ in range(n_col)] for _ in range(n_row)]

    
    # Fill costs in the first row
    for i in range(n_col):
        matrix[0][i] = i

    # Fill costs in the first column
    for j in range(n_row):
        matrix[j][0] = j


    # Fill in other costs
    for i in range(1, n_row):
        
        for j in range(1, n_col):
            
            top_val = matrix[i - 1][j]
            diag_val = matrix[i - 1][j - 1]
            left_val = matrix[i][j - 1]

            character1 = word1[j - 1]
            character2 = word2[i - 1]
            
            computed_cost = 0
            if character1 == character2:
                matrix[i][j] = diag_val
            else:
                matrix[i][j] = min(top_val, diag_val, left_val) + 1
                 
    leven_distance = matrix[n_row - 1][n_col - 1]
    return leven_distance

assert levenshtein('hi', 'hello') == 4
print('Unit test passed')
print(levenshtein('hola', 'hello'))

# Question 4: Answer C