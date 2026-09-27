# demo_2_loops1.py - simple while loop demonstrations

print("First five squared numbers are:\n")

# while/counter loop
counter = 0                     # set loop counter to 0
while counter < 5:              # loop as long as counter is less than 5
    counter = counter + 1       # increase counter by 1
    print(f"{counter} squared is {counter**2}")  # output the square


print("\nAll cubed numbers up to 500 are:\n")
# another while/counter loop with a more complex condition
counter = 1                     # reset loop counter to 1
while counter**3 < 500:         # loop as long as counter cubed is below 500
    print(counter**3)           # output cube of counter
    counter = counter + 1       # increase counter by 1


print("\nEnd of program.")
