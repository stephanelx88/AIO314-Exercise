# Question 11:

def compute_average(list_nums=[0, 1, 2]):
    var = 0

    for i in list_nums:
        var += i

    return var / len(list_nums)

assert compute_average([4, 6, 8]) == 6
print(compute_average())
# Question 11: Answer A