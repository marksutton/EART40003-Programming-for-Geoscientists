Keyword Arguments (kwargs)
=========================

Normally, arguments to functions are given as a comma separated list inside brackets, e.g. 

<pre>value2 = add_two_numbers_and_raise_to_power_of_third_number(a, b, c)
</pre>

This is fine, and is the convention used in most languages, but you do have to remember (or look up) which arguments are which, 
and passing them in the wrong order is easy to do by mistake (and a common source of bugs). 
Python offers an alternative – you can use 'Keyword Arguments' (almost universally referred to as kwargs, because it's a great word). This looks like:

<pre>value2 = add_and_power(add1=a, add2=b, power=c)
</pre>

Using kwargs means (a) it doesn’t matter what order you put the arguments in, and (b) your code is more human-readable, 
as it's obvious what the passed arguments actually are. Not all built-in functions support kwargs, but some do – 
their description will tell you if you look them up. Some modules make heavy use of them, for instance the 
matplotlib library we will look at in session 8. You'll have function calls like:

<pre>plot(fieldmarks, yearmarks, 'bx', markersize=10, markeredgewidth=3, zorder=3)
</pre>

Notice that this mixes traditional ordered-list arguments (the first three), and a bunch of optional kwargs at the end – this is a common pattern.

The good news is that when you write your own functions you get kwarg functionality for free. If you define a function as:

<pre>def add_and_power(add1, add2, power):
    return (add1 + add2) ** power
</pre>

Then the kwargs just take the names you used as arguments. So you can do either

<pre>add_and_power(1, 2, 3)
</pre>

or

<pre>add_and_power(power=3, add1=1, add2=2)
</pre>

Notice in the second example I put the arguments in a different order- remember with kwargs, the order doesn't matter.

Of course, when using kwargs you have to remember the name of the kwarg – but if you get this wrong Python will tell you when it
tries to run the program, and at least this way it's impossible to pass the wrong values by putting them in the wrong order.

It's up to you whether or not you use kwargs in your own programs to call your own functions – but you will sometimes 
have to use them for other people's functions which are designed to use them (like the plotting functions in session 8), 
so you do need to know what they are and how they work.
