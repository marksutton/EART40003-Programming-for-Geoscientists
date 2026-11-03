# Tuples

Tuples are a built-in feature of python – they are like [lists](lists.md), the main difference being that tuples are *immutable* – once you’ve created one you can’t change it. They are used in all sorts of situations where you need to bundle values/objects together.

Tuples can be created like lists, except they use round brackets rather than square brackets. So…

```python
a_tuple = (3, "text", variable_b)
```

…sets one up.

One common use of tuples is for returning multiple values from a [function](user-functions.md), to get round the 'functions return just one value using the return keyword' problem. If you need to return more than one value, just pack your multiple values into a tuple, and return that. Python includes a syntax for extracting values from tuples in these cases:

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

[Return to the site index](index.md)
