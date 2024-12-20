import numpy as np

# Numpy Universal Function
np1 = np.array([-3,-2,-1,0,1,2,3,4,5,6,7,8,9])
print(np1)

# Square root of each element 
#print(np.sqrt(np1))
# 4 ka 4.    aise print

# Absolute Value
#print(np.absolute(np1))

# So x=x*2 sirf numpy arrays pe kaam karega NOT normal lists
'''
# List operation
x = [1, 2, 3]
x = x * 2  # Reassign the modified list back to x
print(x)  # Output: [1, 2, 3, 1, 2, 3]

# Numpy array operation
y = np.array([1, 2, 3])
y = y * 2  # Element-wise multiplication of the array
print(y)  # Output: [2, 4, 6]
'''

# Exponents - e^number
#print(np.exp(np1))

# Min/Max
#print(np.max(np1))
#print(np.min(np1))

# Sign positive or negative - returns -1 or 0
#print(np.sign(np1))

# Trig sin cos log
print(np.log(np1))
#-ve ke liye nan

arr.sum(axis=0)
# along rows jaayega bcs axis=0, so vo har ek column ka sum dega

# arr.flat in NumPy is a flat iterator over a multi-dimensional array, which allows you to iterate through the array as if it were a 1D array, without actually flattening it into a new array.
for item in ar.flat:
  print item

# find the index of the maximum value in an array. 
# agar 2D pe kiya to vo usko flattened array ki tarah dekhke index return karega
arr.argmax()

arr.argmax(axis=0)
# isse vo har column ke max index ko return karega

# The arr.argsort() function in NumPy is used to return the indices that would sort an array.
arr.argsort(axis=-1, kind='quicksort', order=None)
# The axis along which to sort. The default value is -1, which means it will sort the flattened array (1D).

# arr1+arr2 se normal matrix addition - if numpy arrays
# but list1+list2 se list extend ho jaayegi
