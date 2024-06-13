# Question 12:

def get_divisible_by_three(data):
    var = []

    for i in data:
        if i % 3 == 0:
            var.append(i)

    return var
assert get_divisible_by_three([3, 9, 4, 5]) == [3, 9]
print(get_divisible_by_three([1, 2, 3, 5, 6]))

# Question 12: Answer A