# C-1.22
# Write a short Python program that takes two arrays a and b of length n storing int values,
# and returns the dot product of a and b. That is, it returns an array c of length n such that
# c[i] = a[i]·b[i],
# for i = 0,...,n−1.

first = [1, 2, 3, 4]
second = [1, 2, 3, 4]


def dot_product(a, b):
    # assume n is the same for both
    c = []
    for k in range(0, len(a)):
        c.append(a[k] + b[k])
    return c


third = dot_product(first, second)

print(third)
