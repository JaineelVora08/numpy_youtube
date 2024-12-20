import numpy as np

# Slicing Numpy Arrays
np1 = np.array([1,2,3,4,5,6,7,8,9])

# Return 2,3,4,5 - 1:5 me 5 is excluded
print(np1[1:5])
# numbers array ke form me print honge

# Return from something till the end of the array?
# 4-9
print(np1[3:])

# Return Negative Slices
# 7, 8 = -3,-2
# ESSENTIALLY UPPER LIMIT ME SE -1 KARO AND NAYE RANGE ME BOTH LIMITS INCLUSIVE KAR LO
print(np1[-3:-1])

# Steps
print(np1[1:5]) # 2-5
print(np1[1:5:2]) # 2-5 in steps of 2

# Steps on the enitre array
# abhi if we put last limit and steps to last vaala to include nahi hoga to agar last vala bhi include karna ho to use this
print(np1[::2])
print(np1[::3])

# Slice a 2-d array
np2 = np.array([
	[1,2,3,4,5], 
	[6,7,8,9,10]])
# Pull out a single item
print(np2[1,2])

# Slice a 2-d array 2,3
print(np2[0:1, 1:3])
# prints [[2,3]]

# Slice from both rows 2,3 and 7,8
print(np2[0:2, 1:3])
# # prints [[2,3]
	     [7,8]]

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.size)  # Output: 6 (total elements)
print(len(b))  # Output: 2 (number of rows, first dimension)
