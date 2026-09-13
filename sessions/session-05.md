---
course: EART40003
course_title: Programming for Geoscientists
session: 5
year: 2026
author_short: MDS
title: "Session 5: Reference"
subtitle: "Reference and pre-reading"
---

# Definitions

### Import

The process of bringing a module, package, or library into your program so you can use it – this is a general term used in many languages, though most don’t actually use the keyword ‘import’ to do it (Python does).

### Keyword Argument (commonly abbreviated to kwarg)

An alternative syntax for passing arguments to functions or methods. Using kwargs allows you to put arguments in any order, and by providing names for them in your function call, to improve code readability. Not all built-in functions support kwargs, but you can always use them with user-defined functions.

### Kwarg

Abbreviation of *Keyword Argument*

### Module (or package, or library)

A set of functions (and other stuff\*) that you can *import* into your program to provide extra functionality. Package and library are not quite synonyms of module, as both terms can be used for groups of related modules as well as single one. In python, at its simplest, a module is simply a .py file in which functions are defined. \*The ‘other stuff’ sometimes includes definitions of constants (e.g. math.pi), and definitions of classes with methods for complex data-types.

### Tuple

Tuples are ‘lightweight lists’ – they work a lot like lists, except that you can’t change them once they have been created. They are used for, among other things, returning multiple values from functions. Tuples do exist in some other languages, but far from all.

### User Defined Function

A function that you write, as part of your program.

# Functions

I'm not providing any reference materials here – we will be using functions from both the *math* and *random* libraries, but it's time for you to start getting into the habit of looking up what's available and how they work online!

# Topics

## Import

The import keyword is used to import items (functions, classes, constants) from external modules into your program, so you can use them. A single import statement works for the entire .py file. It’s normal to put all required imports right at the start of your files.

To provide flexibility (or to add confusion?) you can use import in several different ways. The simplest is:

::: syntax-template

import module [as alias]     # the 'as alias' is optional

:::

For instance:

```python
import math
import numpy as np
```

Once this is done, you can use anything from the imported module, but you must prefix it with *modulename.* (module name is the name of the module, or the alias if you gave one). So

```python
math.sin(angle)   # use the sin function from math module
np.var(my_data)   # use the var function from numpy module
```

If the need to prefix with *modulename.* annoys you, there is an alternative! You can use:

```python
from module import items
```

Where *module* is a module (like math), and *items* is a comma-separated series of items you want to import. Once this is done, you can use the items WITHOUT the modulename prefix. e.g...

```python
from math import sin, cos, pi
```

… lets you use the sin and cos functions, and the pi constant, without needing to prefix them.

Finally, you CAN also import all items from a module like this, using \*

```python
from math import *
```

`from module import *` is legal Python and you will see it in other people's code, but it is normally best avoided. Importing the module itself, or explicitly importing the particular names you need, makes it much clearer where functions and constants came from and avoids accidental name clashes.

## User-defined functions and return, and local/global variables

Python functions look like:

::: syntax-template

def function_name(argument_list):

    [indented statements forming the body of the function]

:::

*function_name* has the same restrictions as variable names do. Function names, like variable names, should describe what they do. *argument_list* is the list of arguments, separated by commas. The name you use for the argument will become a local variable within the function, holding whatever the value is passed to the function.

Use the *return* keyword to return a value from the function and finish (‘return’ to the code that called the function). The return value can return any Python object you like – typically it will be an int, float, string, or bool, but you can return anything – including a *tuple* if you want to return more than one value (see below). You can have more than one *return* in a function but remember that the function finishes when it reaches the first one. For functions that don’t return a value, you can either use ‘return’ with no value after it, or you can just let execution ‘fall off the end’ of the function. People dispute whether or not it’s good style to use the return keyword in this case, so nothing is proscribed for this course.

Note: The function definition must come earlier in the code than the point where you use it. Normally you define all your functions at the start of the program before you start using any of them.

So:

```python
def add_numbers(number1, number2):
    return number1 + number2
```

Defines a function called *add_numbers* that takes two arguments, and returns their sum. Use it just like any built-in function, e.g.

```python
print(add_numbers(1,10))  # prints 11
```

Inside the function when it’s called, *number1* will take the value of 1, and *number2* will take the value of 10.

Argument names (like *number1* and *number2*) and any variables or objects that are created *inside* the function are *local variables*  - they only exist inside the function, and can’t be referred to outside of it – they are destroyed by the system when the function returns. Also, functions can’t alter any variables that exist in the rest of the program – the idea is that functions are ‘black boxes’ sealed off from the rest of the world, that communicate only through arguments and return values.

> **Technical note — optional:** This 'black box' description is a slight simplification. If you pass a container object like a list into a function, the function **can** modify the contents of that list. There are other exceptions too, but a full explanation, which involves the concepts of value- and reference-passing, is beyond the scope of this course.

You ARE allowed to break this ‘black box’ paradigm and alter variables in the main program, using the *global* keyword. For example:

```python
def add_to_variable_a(b):
    global a
    a += b
    return
```

```python
a = 10
add_to_variable_a(5)
print(a)    # prints 15
```

Using global like this is occasionally convenient, but it’s almost always a bad idea – the black box paradigm exists for a reason, and if you keep breaking it, eventually you will introduce difficult-to-find bugs. It’s almost always better to pass things as arguments instead, and pass values back using return.

### Common errors

- Forgetting the :

- Forgetting to indent

- Forgetting to include a ‘return’ to actually pass your value back

- Trying to alter variables from outside the function without using *global*

- Not testing them properly! To test a function you normally need to write a line or two of main-program code to check it does what it’s meant to. It’s tempting to be lazy and not do this – but it will come back and bite you one day. **Always test ALL functions you write, no matter how trivial they are.**

## Tuples

Tuples are a built-in feature of python – they are like lists, the main difference being that tuples are *immutable* – once you’ve created one you can’t change it. They are used in all sorts of situations where you need to bundle values/objects together.

Tuples can be created like lists, except they use round brackets rather than square brackets. So…

```python
a_tuple = (3, "text", variable_b)
```

…sets one up.

One common use of tuples is for returning multiple values from a function, to get round the 'functions return just one value using the return keyword' problem. If you need to return more than one value, just pack your multiple values into a tuple, and return that. Python includes a syntax for extracting values from tuples in these cases:

```python
value1, value2 = function_that_returns_a_tuple()
```

Assuming the function returns a tuple of length 2, this unpacks it into *value1* and *value2*.

So for example, this short program defines a function that calculates both the square and cube of its argument, and returns them as a tuple. It then uses that function to calculate the square and cube of 3, and prints out the answers

```python
def square_and_cube(a):
     square = a**2  # calculate square of argument
     cube = a**3    # and cube as well
     return (square, cube)  # return them as a tuple
```

```python
s, q = square_and_cube(3)
print(f"square of 3 is {s} and cube of 3 is {q}")
```

## Keyword Arguments (kwargs)

Normally, arguments to functions are given as a comma separated list inside brackets, e.g.

```python
value2 = add_two_numbers_and_raise_to_power_of_third_number(a, b, c)
```

This is fine, and is the convention used in most languages, but you do have to remember (or look up) which arguments are which and passing them in the wrong order is easy to do by mistake (and a common source of bugs). Python offers an alternative – you can use **keyword arguments** (also often informally called *kwargs*). When you call a function using keyword arguments, it looks like:

```python
value2 = add_and_power(add1=4, add2=10, power=2)
```

Using keyword arguments means (a) it doesn’t matter what order you put the arguments in, and (b) your code is more human-readable, as it's obvious what the passed arguments actually are. Not all built-in functions support keyword arguments, but some do – their description will tell you if you look them up. Some modules make heavy use of them, for instance the matplotlib library we will look at in session 8. You'll have function calls like:

```python
plot(fieldmarks, yearmarks, 'bx', markersize=10, markeredgewidth=3, zorder=3)
```

Notice that this mixes traditional ordered-list arguments (the first three), and a bunch of optional keyword arguments at the end – this is a common pattern.

The good news is that when you write your own functions you get keyword-argument functionality for free. If you define a function as:

```python
def add_and_power(add1, add2, power):
    return (add1 + add2) ** power
```

Then the keyword arguments are the names you used as arguments. So you can do *either*

```python
add_and_power(1, 2, 3)
```

or

```python
add_and_power(power=3, add1=1, add2=2)
```

Notice in the second example I put the arguments in a different order- remember with keyword arguments, the order doesn't matter.

Of course, when using keyword arguments you must remember the name of the keyword argument – but if you get this wrong Python will tell you when it tries to run the program, and at least this way it's impossible to pass the wrong values by putting them in the wrong order.

It's up to you whether or not you use keyword arguments in your own programs to call your own functions – but you will sometimes have to use them for other people's functions which are designed to use them (like the plotting functions in session 8), so you do need to know what they are and how they work.

## Custom modules (multi-file projects)

So far, we’ve always written a Python program in a single file. That’s fine when programs are short, but as they get longer you’ll find that it becomes inconvenient – you’ll need to do a lot of scrolling up and down to find code, and it gets unwieldy. You may also find that you have certain functions that you want to make available to more than one program. While you *can* just copy/paste them in whenever you need them, if you make any changes you then have to do that in more than one place

Python makes it easy to create your own modules, and to use this concept to split your code over multiple files (and to use certain modules in more than one program if you want to).

To create a module, all you need to do is to create a python file that defines the functions you want in your module, and make sure it’s in the same folder as your ‘main’ program file. You then import it using the filename (without the .py), in exactly the same way as you would import modules like *math*. So, for example, you might create a file called ‘*squarefunctions.py*’ that looks like:

```python
def square_add_one(value):
    return value**2 + 1
```

```python
def square_minus_one(value):
    return value**2 - 1
```

You could then use your new *squarefunctions* module in a different python file like this:

```python
import squarefunctions as sqf
```

```python
print(sqf.square_add_one(10))
print(sqf.square_minus_one(10))
```
