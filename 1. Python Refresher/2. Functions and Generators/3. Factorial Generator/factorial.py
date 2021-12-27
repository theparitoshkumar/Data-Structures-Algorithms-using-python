""""
In the following exercise, you will create a generator fact_gen() that generates factorials. For a number n, n factorial is denoted by n!, and it is the product of all positive integers less than or equal to n. For example,

5! = 5 * 4 * 3 * 2 * 1 = 120

In this exercise, you will define prod(a, b) which returns the product of numbers a and b. You will also define fact_gen() which yields the next factorial number.
"""

def prod(a,b):
    # TODO change output to the product of a and b
    return a*b

def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        # TODO: update i and n
        # Hint: i is a successive integer and n is the previous product
        i += 1
        n = output


# Test block
my_gen = fact_gen()
num = 5
for i in range(num):
    print(next(my_gen))

# Correct result when num = 5:
# 1
# 2
# 6
# 24
# 120