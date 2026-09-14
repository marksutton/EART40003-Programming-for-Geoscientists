Numpy Functions
=========================

These are provided by the numpy module - so you will need to import it! if you use the traditional numpy import

<pre>import numpy as np</pre>

Then you will need to prefix all functions with `np.`

Note that there also a few methods of the array class - see [numpy array methods](numpy_methods.md) for these.

------------

Functions are given as:

**function_name(arguments) return type: return_type 

**arguments** is the list of arguments the function expects – the text will tell you what they do. I haven’t always documented all arguments.

**return_type** is the type of value the function returns – in many cases this is a string or a number. Some functions do not return any value – these are given as return type: N/A

--------------------

**linspace(start, stop, count) return type: array**
linspace returns a numpy array of count evenly spaced numbers between (and including) the start and stop values. 
For example, `linspace(0,5,10)` returns `[0 0.625 1.25 1.875 2.5 3.125 3.75 4.375 5]`. `linspace` is similar in some ways to the built-in `range` function, 
but returns floating point numbers not integers. It has all sorts of uses – one is in plotting graphs. 
If you have a function that that takes a value x and returns y, just use linspace to generate a range of x values, 
and then use these to generate your y values. NOTE – unlike `range`, the ‘stop’ value for `linspace` IS the last value generated (range stops at the stop value – 1).

**transpose(array) return type: array**
Transposes a multidimensional array (swaps rows and columns]. No effect on one-dimensional arrays.

**zeros(size) return type: array**
`zeros` (make sure you don’t spell it zeroes) creates an array with elements initialised to zero (as a floating point type). 
To create a 1-dimensional array (a vector), just use a number for size, e.g. `zeros(3)` to create `[0 0 0]`.
To create a multidimensional array, pass a tuple as an argument, specifying the sizes of each dimension of the array. 
So for a two-dimensional array (a table) with sizes 10 and 5, use `zeros((10,5))`. Note the double-brackets – 
this is because the argument is a tuple.

**Mathematical functions:**
Numpy includes a lot of maths functions, including pretty well everything that’s in the math module, and some more besides. 
You need the numpy version if you are going to use them with vectorization. I’m not listing these here - 
just look them up, e.g. at (https://www.geeksforgeeks.org/numpy-mathematical-function/)[https://www.geeksforgeeks.org/numpy-mathematical-function/]. 
A lot of these (e.g. sin) have the same name as functions in the math module – if you import both, avoid the import * syntax! You have been warned…
