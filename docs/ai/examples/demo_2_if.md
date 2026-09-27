---
---
{% raw %}
# demo_2_if.py

Return to [Demonstration programs](index.md).

````python
# demo_2_if.py - introduction to if statements

# Use int() to convert to integer - similar to float() but will always round
# down a whole number. e.g. 3 == int(3.5) and 3 == int(3.6)
input_number = int(input("Enter a number: "))      # get number from the user

# note - statement above combines two function calls
# could have written it as:
#
# input_number = input("Enter a number ")
# input_number = int(input_number)


if input_number > 10:      # evaluate condition 'input_number > 10'
    # do this if condition was true...
    print(f"{input_number} is greater than 10")
else:
    # otherwise (i.e. if it was false) do this
    print(f"{input_number} is not greater than 10")

# to demonstrate how program flow works - we always get here
print("Reached end of program")
````
{% endraw %}
