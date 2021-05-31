# coding=utf-8
import random
# R-1.2
# Write a short Python function, is even(k), that takes an integer value and returns True if k is even,
# and False otherwise. However, your function cannot use the multiplication, modulo, or division operators.

def is_even(k):
    return False if k & 1 else True

print(is_even(2))
print(is_even(3))
