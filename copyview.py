import numpy as np

# Copy Vs. View
# copy is normal copy, view me view ya org dono me se kisi me bhi change kiya to dono me changes dikhenge
np1 = np.array([0,1,2,3,4,5])

# Create a view
np2 = np1.view()

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
