# User-defined functions

Python functions look like:

<div class="syntax-template" style="font-family:inherit; background:#f4f7fa; border-left:3px solid #5483bc; padding:0.5em 0.8em; margin:0.8em 0">
<p style="margin:0">def function_name(argument_list):</p>
<p style="margin:0">    [indented statements forming the body of the function]</p>
</div>


*function_name* has the same restrictions as [variable names](variables.md) do. Function names, like variable names, should describe what they do. *argument_list* is the list of arguments, separated by commas. The name you use for the argument will become a local variable within the function, holding whatever the value is passed to the function.

Use the *return* keyword to return a value from the function and finish (‘return’ to the code that called the function). The return value can return any Python object you like – typically it will be an int, float, string, or bool, but you can return anything – including a [*tuple*](tuples.md) if you want to return more than one value. You can have more than one *return* in a function but remember that the function finishes when it reaches the first one. For functions that don’t return a value, you can either use ‘return’ with no value after it, or you can just let execution ‘fall off the end’ of the function. People dispute whether or not it’s good style to use the return keyword in this case, so nothing is proscribed for this course.

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

## Common errors

- Forgetting the :

- Forgetting to indent

- Forgetting to include a ‘return’ to actually pass your value back

- Trying to alter variables from outside the function without using *global*

- Not testing them properly! To test a function you normally need to write a line or two of main-program code to check it does what it’s meant to. It’s tempting to be lazy and not do this – but it will come back and bite you one day. **Always test ALL functions you write, no matter how trivial they are.**

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

[Return to the site index](index.md)
