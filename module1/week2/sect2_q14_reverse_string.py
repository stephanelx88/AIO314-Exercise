# Question 14:

def reverse_string(x):
    reversed_x = ''
    for i in range(len(x) - 1, -1, -1):
        reversed_x += x[i]

    return reversed_x

x = 'I can do it'
assert reverse_string(x) == 'ti od nac I'

x = 'apricot'
print(reverse_string(x))

# Question 14: Answer B