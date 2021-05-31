# C-1.20
# python's random module includes a function shuffle(data) that accepts a list
# of elements and randomly reorders the elements so that each possible order
# occurs with equal probability. The random module includes a more basic function
#  randint(a, b) that returns a uniformly random integer from a to b
# (including both endpoints). Using only the randint function,
#  implement your own version of the shuffle function.

def shufl(data):
    for k in range(0, len(data)):
        random_index = random.randint(0, k)
        tmp = data[random_index]
        data[random_index] = data[k]
        data[k] = tmp


shufl(alpha)
print(alpha)
