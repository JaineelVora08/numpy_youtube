import numpy as np

# np.sort()  Numerical
np1 = np.array([6,7,4,9,0,2,1])
#print(np1)
#print(np.sort(np1))


# Alphabetical
#np2 = np.array(["John", "Tina", "Aaron", "Zed"])
#print(np2)
#print(np.sort(np2))


# Booleans T/F - BCS ALPHABETICAL/0,1 FALSE PEHLE FIR TRUE 
#np3 = np.array([True, False, False, True])
#print(np3)
#print(np.sort(np3))

# NOTE SORT RETURNS A COPY
#print(np1)
#print(np.sort(np1))
#print(np1)

# 2-d
np4 = np.array([[6,7,1,9],[8,3,5,0]])
print(np4)
print(np.sort(np4))
# default me axis = 1
# combined sort nahi honge but inside each individual row sort honge

# 2D ME decscending
# sorted_arr = np.sort(arr)[:, ::-1]  # Sort along axis 1 and reverse

#NOTE: 2D ME 2 types of sorting
# arr = np.array([[3, 1, 4],
#                 [1, 5, 9],
#                 [2, 6, 8]])

# axis=0: Sorts along the columns / within each column (vertical sorting).
# sorted_arr = np.sort(arr, axis=0)
# [[1 1 4]
#  [2 5 8]
#  [3 6 9]]
# Explanation: For each column:
# Column 1: [3, 1, 2] → Sorted: [1, 2, 3]
# Column 2: [1, 5, 6] → Sorted: [1, 5, 6]
# Column 3: [4, 9, 8] → Sorted: [4, 8, 9]

# axis=1: Sorts along the rows / within each row (horizontal sorting)
# [[1 3 4]
#  [1 5 9]
#  [2 6 8]]
# Explanation: For each row:
# Row 1: [3, 1, 4] → Sorted: [1, 3, 4]
# Row 2: [1, 5, 9] → Sorted: [1, 5, 9]
# Row 3: [2, 6, 8] → Sorted: [2, 6, 8]


# for descending order me sort
# M1 - Reverse after sorting
# sorted_arr = np.sort(arr)[::-1]
# NOTE - [::-1] IS USED TO REVERSE
# M2 - sorted_arr = arr[np.argsort(-arr)]


# NOTE:
# To sort the given 2D array arr = [[1,5,4,2], [3,8,7,6]] to get [[1, 2, 3, 4], [5, 6, 7, 8]], you can perform the following steps:

# Flatten the array: First, you need to flatten the 2D array into a 1D array.
# Sort the flattened array: Sort the flattened 1D array.
# Reshape the array back: Finally, reshape the sorted 1D array back into a 2D array with the desired shape.
