Operators
=========

Operators are symbols used to do things to values or variables, e.g. to add them.

= operator
----------
Used to assign values to variables, as a statement in it’s own right. There should always be exactly one variable-name to the left of an ‘=’ operator, 
but to the right can be anything that python can evalulate to a value (another variable, a number, a calculation, a function call, or combinations of these).
If the variable to the left of the = does not yet exist, it is created automatically.

<pre>
my_variable = 10   # create ‘my_variable’ (if it doesn’t already exist) and set it to 10
a_string = "ten"   # assign the string "ten" to variable a_string
50 = my_variable   # illegal – needs a variable to the left of the = (50 is a value)
my_v = 7*3         # do a calculation, assign result to my_v
my_v = v1 + 2      # add 2 to variable v2, assign result to my_v
a = float("10")+1  # convert string “10” to a value, add 1, assign result to a
b = b + 1          # increase value of variable b by 1
b = (c*(a**z))/10.2   # do complex calculation, assign result to b
</pre>

\+ operator
----------
Adds two numbers together. If the values either side of the + are strings, it joins them together instead
<pre>
c = 10 + 2   # Add 10 and 2, put result (12) into variable c
d = x + 6    # If x is a number, value of x + 6 assigned to d. If x is a string this
             # will give an error (strings can only be added to other strings)

e = a + "?"  # If a is a string, put a ? on the end of it and assign that to variable e.
             # If a is a number this will give an error for the same reason as above.
</pre>

+ can also be used to join lists:

<pre>
print([1, 2, 4] + [5, 8, 10])  # Prints [1, 2, 4, 5, 8, 10]
</pre>


\- operator
----------
Performs subtraction. Can only be used on numbers (not strings). 
<pre>
c = e - 2      # Subtract 2 from the value in variable e, assign result to variable c
d = "ten" - 3  # ILLEGAL – can’t subtract from a string
</pre>

\* operator
----------
Performs multiplication. Can only be used on numbers (not strings).
<pre>
print(e * 2)    # Multiply the value in variable e by 2, print it
d = 200 * b     # Multiply b by 200, put result in d
</pre>

/ operator
----------
Performs division. Can only be used on numbers (not strings). Attempting to divide by 0 will generate an error.
<pre>
print(1 / 2)    # Calculate 1/2, print the result (0.5)
v = x / c       # Divide values of x by value of c, put result in v
v = x / 0       # ILLEGAL – you can’t divide by 0.
</pre>

** operator
-----------
Raise a number to the power of another number. You can use negative and non-integer powers.
<pre>
print(10 ** 2)     # prints 10 squared (100)
sqrt_a = a ** 0.5  # Raise a to the power of 0.5 (= square root), put result in sqrt_a
a = b ** c         # work out b to the power of c, put result in a
</pre>

% operator
----------

For numbers, it performs a modulus calculation (i.e. works out the remainder of a division). 
<pre>
print(15 % 6)      # print the remainder when dividing 15 by 6 (3)
a = b % c          # calculate the remainder from dividing b by c, assign it to a.
                   # this assumes b and c are both numbers 
</pre>

For strings, it provides one of (several) ways of inserting values into  strings. This isn't the approach we are using in this course - it's less modern and convenient than the 'f string' approach - but you should be aware of it so you can understand other peoples's code.

You'll see things like:
<pre>
print("Time taken: %f seconds" % (seconds_variable))
</pre>

This puts the value of *seconds_variable* in for the %f 'placeholder', and is equivalent to:
<pre>
print(f"Time taken: {seconds_variable} seconds")
</pre>

You will see more complicated placeholder than %f - these specify things like number of decimal places, and the type of the variable. You can look them up if you need to decypher them!

**NOTE** – because % has a special meaning in strings (see above) – if you want an actual percent symbol, you use %%. This is a common 'gotcha'!
