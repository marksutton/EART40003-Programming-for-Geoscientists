# multidimensional.py - demo of lists of lists (= two-dimensional lists)
# makes a two-dimensional list of numbers 0-50, and their 0-30th powers

# this will be the 'master list'.
numbers_with_powers = list()    # start it off empty
# numbers_with_powers = []  # alternative way to create an empty list

for power in range(0, 31):      # loop 30 times over values 0-30
    power_list = []             # make new list for numbers to this power

    for i in range(0, 51):      # second nested loop to make this new list
        # work out i**power and put it on the end of new list
        power_list.append(i**power)

    # power_list is now numbers 0-50 raised to power
    # add this list as an element of our master list
    numbers_with_powers.append(power_list)


# finished nested loops - numbers_with_powers will now have 31 elements
# each of which is a list of 51 elements
print(numbers_with_powers[0:4])   # print _some_ of the list to check

# Just a lines break to make it easier to read on output
print("\n")

# Test it for some specific values - note order of indexing!
print(f"6 to the power of 2 is {numbers_with_powers[2][6]}")
print(f"50 to the power of 4 is {numbers_with_powers[4][50]}")
print(f"2 to the power of 28 is {numbers_with_powers[28][2]}")

