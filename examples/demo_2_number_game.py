# welcome message
print("\n\nThink of a whole number between 0 and 100 inclusive\n\n")

# set up variables
maximum = 100   # will keep track of highest value the number could take
minimum = 0     # ... and lowest. Initial values to 100 and 0

# main section - loop round guessing numbers
while True:     # loop forever (or until we get out with break)
    # work out guess - average of minimum and maximum
    # int converts to an integer - and +.5 to round to nearest
    guess = int(((maximum-minimum)/2 + minimum)+.5)

    # tell user the guess and get their input (y,l or h)
    user_input = input(f"Is your number {guess}? "
                       "Enter y for yes, l if it's lower, h if it's higher: ")

    if user_input == "y":            # user typed 'y' - we were right!
        print("Hah! I got it!\n\n")  # victory message
        break                        # get out of the loop to stop program
    elif user_input == "h":
        # it was higher - so minimum is one more than our last guess
        # set new minimum for next time round loop
        minimum = guess+1
    elif user_input == "l":
        # it was lower so set maximum to one less than the guess
        # set new maximum for next time round loop
        maximum = guess-1
    else:
        # must have been a user error!!!
        # users are error prone, so all programs should try to deal
        # with their mistakes in some sensible way. Here we will print an
        # error message, then loop back round so they can try again
        # so ask them again in next loop around
        print("Woops! I can't understand that last input, please try again.")
        # As this is the end of the loop - it will automatically go back
        # round again
