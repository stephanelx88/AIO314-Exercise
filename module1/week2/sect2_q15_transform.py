# Question 15:

def convert_letter(x):
    if x > 0:
        return 'T'
    
    return 'N'

def transform(data):
    res = [convert_letter(x) for x in data]

    return res


data = [10, 0, -10, -1]
assert transform(data) == ['T', 'N', 'N', 'N']

data = [2, 3, 5, -1]
print(transform(data))

# Question 15: Answer C