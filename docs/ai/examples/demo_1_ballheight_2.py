# ballheight.py - Exercise 1b with input function

# set up the 'constant variable'
acceleration_due_to_gravity = 9.81

# get values from the user
# input function - argument is a string - text that appears in the terminal
# input function has a RETURN VALUE - the text that the user types in
# When function runs it 'becomes' the return value...
# ... which you need to do something with. Here I put it into variables
initial_velocity = input("Initial velocity (m/s)? ")
time = input("Time (s)? ")

# This won't work - uncomment to see why
# print(initial_velocity*time)

# input always gives a string. Need to convert to a number
# using the float function
initial_velocity = float(initial_velocity)    # convert string input to number
time = float(time)                            # and again for the other one

# do the calculation
height = initial_velocity*time - (1/2)*acceleration_due_to_gravity*time**2

# formatted print for the output
print(f"After {time}s, height is {height:.2f}m")
