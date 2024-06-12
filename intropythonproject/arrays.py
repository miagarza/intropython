import numpy as np
#"as np" allos us to refer to numpy as np

#arrays are a list of items

arr = np.array([1,2,3,4,5,6])
print(arr)
#created an empty array

#size of array: how many values are in the array
print(arr.shape)

# Two dimensional array
#An array that stores arrays, lists of lists

twoDarr = np.array([[1,2,3,], [5,6,7,], [9,10,11]])
print(twoDarr)
print(twoDarr.shape)
#shape= (2,3): 2 lists, 4 values each