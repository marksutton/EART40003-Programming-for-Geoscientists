# ballheight.py - Exercise 1b

# set up variables - note proper names, using snake_case
acceleration_due_to_gravity = 9.81
time = 0.9
initial_velocity = 7.1

# do calculation
height = initial_velocity*time - (1/2)*acceleration_due_to_gravity*time**2

# Alternative version - also works... and easier to find errors!
# gt_squared = acceleration_due_to_gravity*time**2
# height = initial_velocity*time - 0.5 * gt_squared

print(height)

# A better print - formatted output to reduce decimal places, with some text
print(f"At t={time}s, height is {height:.2f}m")
