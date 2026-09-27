# float_fail.py - limitations of floating point numbers

a = 0.0         # start a at 0 (as a float)
counter = 0     # start counter at 0

while counter < 1000000:     # loop a million times
    a = a + 0.000001         # add one-millionth each time
    counter = counter + 1    # increment counter

# a should now be one shouldn't it?
if a == 1:
    print("a is 1")          # this should print
else:
    # ... BUT actually a ISN'T 1, and we get here...
    print(f"oops, a is NOT 1, it's {a}")

# https://docs.python.org/3/tutorial/floatingpoint.html for full explanation



