# lists.py - basic list usage

numbers_list = ["zero", "one", "two", "three", "four"]
numbers_list += ["five", "six"]

# var += value is a shorthand for var = var + value. Works for *=, /=, -= too

numbers_list.append("seven")    # append method adds an element


final_two = ["eight", "nine"]
numbers_list.extend(final_two)  # extend adds another list (alternative to +)

print(numbers_list)       # prints the whole list ['zero', ... 'nine']

print(numbers_list[3])    # prints 'three'

# use list 'slicing' - exactly the same syntax as string slicing
print(numbers_list[:4])   # prints a list ['zero', 'one', 'two', 'three']

if "two" in numbers_list:   # 'in' condition - true if "two" exists in list
    print("Found 'two' in the list")

for digit in numbers_list:
    # loop over numbers_list - digit is the element each time round

    # print element - and find it's index using 'index' method of list
    print(f"{digit} is digit number {numbers_list.index(digit)}")

print()  # blank line
# There is a second approach to looping over a list...

for i in range(len(numbers_list)):
    print(f"{numbers_list[i]} is digit number {i}")

# Here I use a for loop with range to generate a variable 'i' that
# goes from 0 to 9. The len function gives me the number of elements in
# the list, and range gives me 0 to length -1, so as length is 10 that
# gives me 0 to 9, which is what I want.

# Could have done this with while loops of course:
i = 0
while i < len(numbers_list):
    print(f"{numbers_list[i]} is digit number {i}")
    i += 1
# ... but for/range version is shorter, and more commonly used


# Looping using an index like this rather than looping over the elements
# themselves as I did in the first example is often useful - sometimes you
# will _want_ the index, and while you can find it with the index method
# that will not work if you have identical elements in your list

# NOTE - While I'm generally encouraging you not to abbreviate
# variables too much, using 'i' for an index variable like this is SO
# standard in programming that it's definitely OK
