# C-1.24
# Write a short Python function that counts the number of vowels in a given
# character string.
#
given_string = "There are 9 vowels in this string"
count = 0

for c in given_string:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == "u":
        count += 1

print(count)
