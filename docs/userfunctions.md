Functions and local/global variables
===================================

Python functions look like:

<pre>def function_name(argument_list):
    [indented statements forming the body of the function]
</pre>

_function_name_ has the same restrictions as variable names do. 
Make function names at least slightly descriptive of what they do. 
_argument_list_ is the list of arguments, separated by commas. 
The name you use for the argument will become a local variable (see below) within the function, 
with the value passed at that point.

Use the return keyword to return a value from the function and finish 
(‘return’ to the code that called the function). 
You can return any Python object you like – 
including [a tuple](tuples.md) if you want to return more than one value. 
You can have more than one return in a function, but remember that the function 
finishes when it reaches the first one. For functions that don’t return a value, you 
can either use ‘return’ with no value after it, or you can just let execution 
‘fall off the end’ of the function.
People dispute whether or not it’s good style to use the return keyword in this case, 
so nothing is proscribed for this course.

Note: The function definition has to come earlier in the code than the point where you use it. 

So:

<pre>def add_numbers(a, b):
    return a+b
 </pre>
 
Defines a function that takes two arguments, and returns their sum. Use it just like any built-in function, e.g.

<pre>print(add_numbers(1,10))  # prints 11
</pre>

Inside the function when it’s called, a will take the value of 1, and b will take the value of 10.

Argument names (like a and b) and any variables or objects that are created inside the 
function are **local variables**  - they only exist inside the function, and can’t be referred 
to outside of it – they are destroyed by the system when the function returns. Also, 
functions can’t alter any variables that exist in the rest of the program – 
the idea is that functions are ‘black boxes’ sealed off from the rest of the world, 
that communicate only through arguments and return values. 

You ARE allowed to break this black box paradigm and access variables in the main program, 
using the global keyword. So the following code works as it looks like it will

<pre>def add_to_variable_a(b):
    global a
    a += b
    return

a = 10
add_to_variable_a(5)
print(a)    # prints 15
</pre>

Using global like this is sometimes convenient, but it’s not normally a good idea – 
the black box paradigm exists for a reason, and if you keep breaking it, eventually 
you will introduce difficult-to-find bugs. Try to use return values and argument passing instead.

Common errors with functions
*	Forgetting the :
*	Forgetting to indent
*	Forgetting to include a ‘return’ to actually pass your value back
*	Trying to alter variables from outside the function without using global
*	Not testing them properly! To test a function you normally need to write a line or two of main-program code to check it does what it’s meant to. It’s easy to be lazy and not do this – but it will come back and bite you one day. Always test ALL functions you write, no matter how trivial they are.
