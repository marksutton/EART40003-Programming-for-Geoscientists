
# numpydemo3.py - speed of vectorization

import numpy as np
import time                          # for timing functions

big_array = np.linspace(0, 1000, 50000000)   # 50 million elements
big_list = list(big_array)                   # make a list version too


# add 1 to each element in three different ways, showing time taken

# (a) using lists...
print("Adding 1 using lists")
start = time.perf_counter()                 # record start time

# do addition with a for loop
for index in range(len(big_list)):
    big_list[index] += 1

time_taken = time.perf_counter() - start    # work out time taken
print(f"Done in {time_taken:.2f}s")       # ... and print

input("Return to continue")  # pause


# (b) using lists comprehensions
print("Adding 1 using list comprehensions")  # comprehensions better?
start = time.perf_counter()

# do addition with a comprehension
big_list_2 = [value + 1 for value in big_list]

time_taken = time.perf_counter() - start
print(f"Done in {time_taken:.2f}s")  # time taken as before

input("Return to continue")

# (c) using arrays and vectorization
print("Adding 1 using array vectorization")
start = time.perf_counter()

big_array += 1      # add 1 to all elements of array

time_taken = time.perf_counter() - start
print(f"Done in {time_taken:.2f}s")   # as before
