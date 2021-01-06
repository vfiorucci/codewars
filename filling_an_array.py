"""Fill an array.

Description:
We want an array, but not just any old array, an array with contents!
Write a function that produces an array with the numbers 0 to N-1 in it.
For example, the following code will result in an array containing the numbers 0 to 4:
arr(5) // => [0,1,2,3,4]
"""
def arr(n=0):
    """Loop through array."""
    array = []
    for i in range(n): array.append(i)
    return array
    # This was what I was going for
    # return [i for i in range(n)]

result = arr(5)
print(result)


# Other Solutions:

# 1. 
# def arr(n=0):
#     return list(range(n))

# 2. 
# def arr(n=0): 
#     return [i for i in range(n)]

# 3. 
# def arr(n=0): 
#     return [*range(n)]

# 4. 
# def arr(*n): 
#     return list(range(sum(n)))