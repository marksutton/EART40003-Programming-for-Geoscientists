# fibonacci.py - generate a Finonacci series
# each number is the sum of the last two in the series

fibonacci = [0, 1]  # seed the list

for i in range(100):    # loop 100 times
    # create and append new Fibonacci number
    fibonacci.append(fibonacci[-1]+fibonacci[-2])

# print it to check
print("First 100 Fibonacci numbers:")
print(fibonacci)

# QUESTION - it would be good to print it in a nicer format, without the []
# Could we just use join method to make a string with ", " separators?
# i.e.
# print(", ".join(fibonacci))
# ... no, this doesn't work. Why not??

# Second part - user input with checking
while True:  # infinite loop (exited with a break)
    try:
        # get value
        min_value = float(input("Enter minimum value for a Fibonacci number "))
        # no exception thrown, so done, exit the loop
        break
    except Exception:
        # error - and will go back round loop
        print("Not a valid value, try again!")

# find correct value in list
for value in fibonacci:     # loop over all values
    if value >= min_value:  # if it's over the minimum...
        # print it out
        print(f"First Fibonacci number greater than or equal to {min_value}"
              f" is {value}")
        # and stop the loop - don't want to check/print any more
        break

