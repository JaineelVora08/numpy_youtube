import numpy as np

# Search
np1 = np.array([1,2,3,4,5,6,7,8,9,10, 3])

#x = np.where(np1 == 3)
#tuple of index nos - (array([ 2, 10]),dtype=int64)

#print(np1)
#print(x[0]) = prints [2 10] ie index number
#print(np1[x[0]]) = [3 3]

# If you want to extract the elements that satisfy the condition (i.e., the actual 3s), you can use the result of np.where() to index the array:
# values = np1[np.where(np1 == 3)]
# print(values)
# [3 3]


# Return even items
#y = np.where(np1 % 2 == 0)
#print(np1)
#print(y[0]) - isse indices print honge NOT THE VALUES

# Return odd items
z = np.where(np1 % 2 == 1)
print(np1)
print(z[0])
