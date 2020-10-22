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
Does COMPLETELY different things with numbers and strings! 
<br />
For numbers, it performs a modulus calculation (i.e. works out the remainder of a division). 
For strings, it allows the insertion of values into the string using formatted output. 
Put the ‘base’ string to the left of the %, and include placeholders (see below). 
To the right of the %, put the values to go into the string, inside brackets, and separated by commas (
technically this is a tuple – more on tuples later in the course). Common placeholders are:
<br />
* %g: use to just insert numbers without playing with decimal places at all. Note that for big numbers, Python will revert to exponent format (see %e below), which you might not want, so for integers you can use…
* %d: use to display an integer, i.e. a number without decimal places. %g works for integers as well, but %d never uses exponent format (see %e below). 
* %f: use to control the number of decimal places. Normal format is %.nf, where n is the number of decimal places you want. E.g. %.3f for three decimal places.
* %e: use for exponent (‘scientific’) format – good for very large or very small numbers. You can specify the number of decimal places you want. E.g. %.2e gives you exponent format with two decimal places. As this is output as text (without superscripts) it can’t generate this as something like 3.56 x 103. Instead you get 3.56e3 or 3.56e03, which is meant to mean the same thing. 
* %s: use to insert a string (obviously you have to make sure the value passed is a string)
<br />
NOTE – because % has a special meaning in strings – if you want an actual percent symbol, you use %%. See e.g. https://www.python-course.eu/python3_formatted_output.php 
for a more complete list of examples and format ‘placeholders’ (and for another way of doing formatting – the % method is not the only one available). 
<pre>
print(15 % 6)      # print the remainder when dividing 15 by 6 (3)
a = b % c          # calculate the remainder from dividing b by c, assign it to a.
                   # this assumes b and c are both numbers 
</pre>
<br />
[String examples below assume variable b holds number 3.553, variable s holds string “hello”]
<pre>		
print("Value is %g" % (10.2))                 # prints ‘Value is 10.2’
print("Values are %g and %g” % (10.2, 5.3))   # prints ‘Values are 10.2 and 5.3’
print("b is %g%%” % (b))                      # prints ‘b is 3.553%’
print("String s is %s” % (s))                 # prints ‘String s is hello’
s2 = "%g,%g" % (b, 10.2)                      # sets s2 to ‘3.553,10.2’
s2 = "%g,%g" % (b, s)                         # ILLEGAL - %g can’t display string s
print("b to 2dps is %.2f" % (b))              # prints ‘b to 2dps is 3.55’
print("b to 1dp is %.2f" % (b))               # prints ‘b to 1dp is 3.6’
print("b x 1000 is %.1e" % (b*1000))          # prints ‘3.6e+03’ (meaning 3.6 x 103)  
print("A big number: %d” % (100000000))       # prints ‘A big number: 100000000’
</pre>
