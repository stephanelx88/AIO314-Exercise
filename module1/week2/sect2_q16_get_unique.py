# Question 16:

def is_not_in(x, data):
    for i in data:
        if x == i:
            return 0
    return 1

def get_unique(data):
    res = []

    for i in data:
        if is_not_in(i, res):
            res.append(i)

    return res
lst = [10, 10, 9, 7, 7]
assert get_unique(lst) == [10, 9, 7]

lst = [9, 9, 8, 1, 1]
print(get_unique(lst))

# Question 16: Answer A