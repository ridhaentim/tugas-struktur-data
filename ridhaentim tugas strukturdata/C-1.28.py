#C-1.28 
# For the special case of p = 2, this results in the traditional Euclidean norm, which represents the length of the vector. 
#For example, the Euclidean norm of a two-dimensional vector with coordinates (4,3) has a Euclidean norm of√42 +32 =√16+9 =√25 = 5. 
#Give an implementation of a function named norm such that norm(v, p) returns the p-norm value of v and norm(v) returns the Euclidean norm of v.

n=[1,2,3,4,5] # You can create a custom list by using for loop and append

def norm(n,p=2):
    sum = 0
    for i in n:
        sum += i**p
    return sum ** (1/p)

print(norm(n))
print(norm(n,3))

You may assume that v is a list of numbers.
