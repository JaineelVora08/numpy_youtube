import numpy as np

# reshape se view banega NOT copy

# Create 1-D Numpy Array and Get Shape
np1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(np1)
print(np1.shape)

# Create 2-D Array and get Shape, (rows/columns-elements)
#np2 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
#print(np2)
#print(np2.shape)
 
# Reshape 2-D
#np3 = np1.reshape(3,4)
#print(np3)
#print(np3.shape)

# Reshape 3-D
np4 = np1.reshape(2,3,2)
print(np4)
print(np4.shape)

# Flatten to 1-D
# always Reshapes the array np4 into a 1D array (flat array) 
# The -1 tells NumPy to infer the size of the new dimension automatically based on the original array's size.
np5 = np4.reshape(-1)
print(np5)
print(np5.shape)

# The arr.ravel() function in NumPy is used to return a flattened view (or copy) of a multi-dimensional array. This means it converts a multi-dimensional array (e.g., a 2D or 3D array) into a 1D array.
arr = np.array([[1, 2, 3], [4, 5, 6]])
flat_arr = arr.ravel()


