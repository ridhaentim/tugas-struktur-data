# R-1.7

# give a single command that computes the sum from r-1.6, relying on python's comprehension syntax and built in sum function



def sum_of_squares_odd2(n):
    return sum([k * k for k in range(0, n) if k % 2 != 0])


print(sum_of_squares_odd2(4))
