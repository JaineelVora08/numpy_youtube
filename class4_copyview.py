import numpy as np

# Copy Vs. View
# copy is normal copy, view me view ya org dono me se kisi me bhi change kiya to dono me changes dikhenge
np1 = np.array([0,1,2,3,4,5])

# Create a view
np2 = np1.view()

# SLICING ARRAY ALSO CREATES VIEW
# rr = np.array([1, 2, 3, 4, 5])
# view_arr = arr.view()
# slice_arr = arr[1:4]

# view_arr[0] = 99  # Modify the view
# slice_arr[0] = 88  # Modify the slice
# isse jo org array me element tha vo bhi change hoga

# print("Original:", arr)  # Output: [99 88 3 4 5]
# print("View:", view_arr)  # Output: [99 88 3 4 5]
# print("Slice:", slice_arr)  # Output: [88 3 4]

# you can directly print lists/arrays in python
# list can have different data types

print(f'Original NP1 {np1}')
print(f'Original NP2 {np2}')

np2[0] = 41

print(f'Changed NP1 {np1}')
print(f'Original NP2 {np2}')


'''
# Create a Copy
np2 = np1.copy()
print(f'Original NP1 {np1}')
print(f'Original NP2 {np2}')

np2[0] = 41

print(f'Changed NP1 {np1}')
print(f'Original NP2 {np2}')
'''

#To check
If array.base is None, the array is a standalone object (a copy).
If array.base is not None, the array is a view, and array.base points to the original data it references.
