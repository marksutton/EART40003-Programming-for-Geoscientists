---
---
{% raw %}
# demo_7_numpy1.py

Return to [Demonstration programs](index.md).

````python
# demo_7_numpy1.py - array construction, shape, slicing

import numpy as np   # np alias is standard practice

an_array = np.array([1, 4.3, 5, 8.4, 12.2])  # make array from a list
print(an_array)                              # print it


# linspace makes arrays of number sequences
print(np.linspace(0, 10, 21))

print(np.zeros(10))              # zeros makes arrays of zero values

print(an_array[3])               # indexing works
print(an_array[2:])              # as does slicing


for i in an_array:               # for loops work
    print(i)


# 2d arrays

# make a 2d array from nested lists, and print to show
two_d_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(two_d_array)


# indexing in 2d - slightly different syntax to lists
# which use [1][3]. That DOES still work for arrays
# but this alternative notation probably better.
# Note also - rows are first dimension
print(two_d_array[1, 3])    # prints '8' - row index 1 at poistion index 3

print(two_d_array.shape)  # print sizes of the two dimensions as a tuple (3, 4)
print(f"Columns: {two_d_array.shape[1]}")  # index the tuple to get columns


one_d_array = np.linspace(1, 12, 12)    # make array [1 2 3 ... 12]
print(one_d_array)  # print to check

new_array = one_d_array.reshape(2, 6)   # reshape it to 2D (2 rows, 6 cols)
print(new_array)                      # print reshaped array

new_array = new_array.transpose()       # transpose
print(new_array)        # show transposed (6 rows, 2 cols)


zero_array = np.zeros((2, 4))           # make array of zeros, 2 rows, 4 cols
print(zero_array)                       # show it
````
{% endraw %}
