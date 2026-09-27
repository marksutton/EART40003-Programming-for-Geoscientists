---
---
{% raw %}
# demo_5_functions.py

Return to [Demonstration programs](index.md).

````python
# functions.py - demo of basic function syntax and usage

# --------------------------------------------------------------------------- #
# My Custom Functions
# --------------------------------------------------------------------------- #

# Custom function that prints a line of - symbols
# No arguments or return value as it directly prints to output.
def print_spacer():
    line_string = ""          # empty string
    for i in range(80):
        line_string += "-"    # add 80 "-" symbols to it
    print(line_string)        # print line of - symbols
    return                    # function finished - return
    # note - return at end is not required if no value returned


# Custom function that prints prettified title - expects string as argument
def print_title(title):
    print_spacer()          # can use a function inside another
    print("***** " + title.upper() + " *****")    # print the title
    print_spacer()          # and another spacer
    return                  # done - not returning a value, so return optional


# Custom function returning a bool
# This assumes it has been passed an integer as an argument
def is_odd(number):
    if number % 2 == 0:
        return False    # even - return False
    else:
        return True     # odd - return True


# Custom function to error checked the user input.
# Returns an integer between the minimum and maximum value.
# If integer entered is outside range, returns minimum or maximum.
# Code very similar to errors.py from session 3.
def integer_input(text, minimum, maximum):
    ok_flag = False     # a 'flag' - bool used to control program
    while ok_flag is False:  # as long as flag is false
        try:
            # try the input and the conversion.
            input_value = float(input(f"{text} ({minimum}-{maximum}) "))

            # will get here if that didn't throw exception
            if not input_value.is_integer():
                # if it wasn't an integer...
                print("Not a whole number, try again\n")
            else:
                # it WAS an integer... in range?
                if input_value < minimum:
                    print("Too low, using minimum\n")
                    return minimum
                elif input_value > maximum:
                    print("Too high, using maximum\n")
                    return maximum
                else:
                    # If we get here it's fine - set flag to True...
                    # ... which will stop the loop
                    ok_flag = True
        except ValueError:
            # catch the conversion error
            print("Not a number, try again\n")
    # We are now back outside the loop... return a value.
    return input_value  # done - return the value


# --------------------------------------------------------------------------- #
# My Main Program
# --------------------------------------------------------------------------- #

# main program execution will start here
print_title("Function demo program")    # print title

# first use of integer_input - use arguments as normal
a = integer_input("Enter number", 1, 10)

# use it again - this time use kwargs in the function call
b = integer_input("Enter second number", maximum=100, minimum=10)

# use is_odd function to check them...
if is_odd(a) and is_odd(b):
    print("Both your numbers are odd")
elif is_odd(a) or is_odd(b):
    print("One of your numbers is odd")
else:
    print("Both of your numbers are even")

# finish with a line of '-' symbols
print_spacer()
````
{% endraw %}
