# Question 13:

def factorial(y):
    var = 1

    while y > 1:
        var *= y

        y -= 1
    return var
assert factorial(8) == 40320
print(factorial(4))

# Question 13: Answer C