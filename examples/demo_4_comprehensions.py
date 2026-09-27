# comprehensions.py - some list comprehension examples

# simple use - put all values of range(10) into a list
zero_to_nine = [x for x in range(10)]
print(zero_to_nine)

# as above, but add one to each
one_to_ten = [x + 1 for x in range(10)]
print(one_to_ten)


# Make a list of zeroes - still need 'x' in 'for' even though not used
ten_zeroes = [0 for x in range(10)]
print(ten_zeroes)


# use 'if' clause of comprehension to filter values
one_to_ten_except_three = [x + 1 for x in range(10) if x != 2]
print(one_to_ten_except_three)


# more complex condition - but same idea
# NOTE - this line would be too long if left 'untreated'
# So I've split it. See reference handout/website for details on
# splitting long lines.
cube_numbers_divisible_by_seven = [val**3 for val
                                   in range(1, 100)
                                   if val**3 % 7 == 0]
print(cube_numbers_divisible_by_seven)
