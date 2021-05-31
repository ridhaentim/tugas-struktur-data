# C-1.18
# Demo list comprehension to create the following
# list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

print([k * (k - 1) for k in range(1, 11)])
