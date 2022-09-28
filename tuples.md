Tuples
======

Tuples are a built-in feature of python – they are similar to lists, the main difference being that tuples are immutable – 
once you’ve created one you can’t change it. They are used in all sorts of situations where you need to bundle values/objects together.

Tuples can be created like lists, except they use round brackets rather than square brackets. So…

<pre>a_tuple = (3, "text", variable_b)
</pre>

... sets one up. Like lists, tuples can have as many elements as you like, and the elements don't all have to be of the same type.
<br />
A common use is for returning multiple values from a function, to get round 
the 'functions return just one value using return keyword' problem. Just pack your multiple values into a tuple, and return that. 
Python includes a syntax for extracting values from tuples in these cases:

<pre>value1, value2 = function_that_returns_a_tuple()
</pre>

Assuming the function returns a tuple of length 2, this unpacks it into value1 and value2.
