# Question 7:

def concat(x, y):

    x.extend(y)

    return x

list_num1 = ['a', 2, 5]
list_num2 = [1, 1]
list_num3 = [0, 0]

assert concat(list_num1, concat(list_num2, list_num3)) == ['a', 2, 5, 1, 1, 0, 0]

a = [1, 2]
b = [3, 4]
c = [0, 0]
print(concat(a, concat(b, c)))

# Question: Answer A
