# R-1.12

# Python's random module includes a function choice(data) that returns a random element
# from a non-empty sequence. The random module in- cludes a more basic function randrange,
# with parameterization similar to the built-in range function, that return a random choice
# from the given range. Using only the randrange function, implement your own version of the choice function.


def my_choice(data):
    return data[random.randrange(0, len(data) - 1)]


print(my_choice(alpha))
