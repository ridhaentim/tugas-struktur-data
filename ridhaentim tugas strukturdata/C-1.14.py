# C-1.14
# Write a short Python function that takes a sequence of integer values and determines
# if there is a distinct pair of numbers in the sequence whose product is odd.

def odd_pair(data):
    count = 0
    for k in range(0, len(data) - 1):
        if k % 2 != 0:
            count += 1
    return True if count >= 2 else False


evens = [2, 4, 6, 8]
print(odd_pair(my_list))
print(odd_pair(evens))
