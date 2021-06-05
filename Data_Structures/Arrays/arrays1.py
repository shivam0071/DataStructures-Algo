# Different arrays in Python

end = "\n" + "*" * 20 + " {} " + "*" * 20 + "\n"

# 1.)  LIST
# A list is a dynamic array
# Mutable and hetrogenous(elements are loosly packed), takes up more space (8-bytes)
# can be used in a variety of situations
# Its better to use NUMPY ARRAYS as they are 50 times faster than lists
# and are stored in continous memory locations

print(end.format("LIST"))
ls = [1,2,'Shivam', lambda x: x*2]
print(ls)
print(ls[3](20))
print(end.format("TUPLE"))
# 2.)  Tuples
# Tuples are immutable and are also hetrogeneous ..they take less space than list
# can be used when the number of elements are fixed

tup = (1,2,"Shivam", lambda x: x * 10)
print(tup)
print(tup[3](10))
print(end.format("Array.Array"))

# 3.) arrays.arrays
# Similar to list but can have only one type of data.
# they takes less space and elements are tightly bounded
# Use this for performance boost
# https://docs.python.org/3/library/array.html?highlight=arrays
# Arrays are sequence types and behave very much like lists, except
# that the type of objects stored in them is constrained

import array
arr = array.array('f', (1.0, 2.0, 3.2,))
print(arr)
arr2 = array.array('i',(1,2,3))
print(arr2)
print(end.format("Strings"))


# Strings
# String are Immutable Arrays of Unicode Characters

print(end.format("Bytes"))
# Bytes – Immutable Arrays of Single Bytes
# Bytes objects are immutable sequences of single bytes (integers in the range of 0 <= x <= 255). Conceptually they’re similar to str objects and you can also think of them as immutable arrays of bytes.
byt = bytes((0, 1, 2, 3))
print(byt)
print(byt[2])
print(end.format("Bytearray"))

#BytArray
# The bytearray type is a mutable sequence of integers in the range 0 <= x <= 255. They’re closely related to bytes objects with the main difference being that bytearrays can be modified freely—you can overwrite elements, remove existing elements, or add new ones. The bytearray object will grow and shrink appropriately./

byt2 = bytearray((0, 1, 2, 3))
print(byt2)


print(end.format("NUMPY ARRAYS"))
# NUMPY ARRAYS are 50 times faster than lists 
import numpy as np
arr = np.array([5, 3, 2, 50, 2])
print(arr)

print(arr, arr.min(), arr.max(), arr.sum())