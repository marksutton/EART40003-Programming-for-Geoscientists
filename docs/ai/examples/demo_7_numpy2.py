# numpydemo2.py - vectorization and conditional indexing

import numpy as np
import math

# make test array - all shown on 1d array, works same on 2d or more
test_array = np.linspace(0, 100, 11)   # make [0 10 20 ... 100]

# conditional indexing
# basic conditions - used to filter an array by a condition
filtered_test_array = test_array[test_array >= 90]
print(filtered_test_array)  # now [90 100]


filtered_test_array_2 = test_array[test_array % 30 == 0]
# filtered_test_array_2 now [0 30 60 90]
print(filtered_test_array_2)


# filtering again with compound conditions
# note: 1. Use of | for 'or' (use & for and)
# note: 2. Brackets around separate conditions - required
filtered_test_array_3 = test_array[(test_array**2 < 200) | (test_array > 85)]

# filtered_test_array_3 now [0 10 90 100]
print(filtered_test_array_3)


# conditional indices to left of = are used to set selected elements
test_array[test_array <= 30] = -1
# test_array now [-1 -1 -1 -1 40 50 ... 90 100]
print(test_array)


# vectorization - mathematical operations on all elements at once

# re-set test array
test_array = np.linspace(0, 100, 11)   # remake [0 10 20 ... 100]

# use maths on an array - affects the entire array
array_plus_one = test_array + 1       # makes [1 11 21 ... ]
print(array_plus_one)

# *=, /=, +=, -= all work too
test_array *= 5   # test_array now [0 50 100 ... 500]
print(test_array)

# add two arrays - adds elements separately
# arrays have to be the same size
test_array += np.linspace(0, 10, 11)
# test_array now [0 51 102 153 ... 459 510]
print(test_array)


# also works with /, -, *
# divide [0 1 2 .. 10] by [10 11 12 ... 20]
division_results = np.linspace(0, 10, 11) / np.linspace(10, 20, 11)
print(division_results)   # [0 0.909 0.167 0.231 ... 0.475 0.5]


# works with _some_ functions - they have to be vectorization-aware
print(np.sin(division_results))       # Prints sines of everything in array
# print(math.sin(division_results))   # FAILS - math functions not usable


# using a custom function with vectorization

# define the function
def volume_of_sphere(r):
    return 4/3 * math.pi * (r**3)


# test on single value
print(f"Volume of sphere radius 5 is {volume_of_sphere(5):.2f}")

# test on an array...
print("Volumes of spheres radius 1-10:")
print(volume_of_sphere(np.linspace(1, 10, 11)))
# works - but how??
