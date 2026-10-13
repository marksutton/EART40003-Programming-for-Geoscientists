# Objects in Python

Python is an Object-Oriented (OO) language, and pretty well everything in Python (including variables which we have thought of as ‘just numbers’) is actually an object. We’ve been calling them variables and thinking of them as just boxes to store things in for (a) simplicity, and (b) compatibility with other languages, in which simple non-object variables normally DO exist. Also, for most of them, most of the time, you don’t have to worry about or care about that fact that they are actually objects.

Objects can be thought of as data with associated functions that can manipulate that data (called ‘methods’ - see [Method](definitions.md#method)). See [Object](definitions.md#object) and [Class](definitions.md#class) in the definitions for more on these concepts. Most ‘basic’ Python variable data-types don’t have many methods that we need in this course (I only give one for *float*, and none for bool or int), but *str* (string) objects are the exception – there are a host of string methods, many of which are very handy indeed. Some are given [under String methods](strings.md#string-methods) – others are available in many different online guides.

To use a method of an object, use the ‘.’ notation – ‘object.method’. So to use the upper() method of the a string object, use **my_string.upper()**. This ‘.’ notation is one of the very few bits of syntax that is almost completely standard in computing – it’s used in pretty well all programming languages that include the concept of objects.

```python
my_string = "brachiopod"
my_string = my_string.upper()
print(my_string)   # prints ‘BRACHIOPOD’
```

The most common question with objects is ‘What ARE the methods I can use with this object, and what arguments do they take’? The best answer is ‘Google them’ – there are many reference documents out there. Obviously to do this you DO need to make sure that you know what the type (i.e. class name) of the object actually is – to find this, look in the Thonny variables window, or for more obscure types not listed there, use `print(type(my_object))`.

NOTE – Python provides an alternative syntax for calling methods – **mystring.upper()** can also be written as **str.upper(mystring)**  (str being the name of the string class). This is not encouraged in this course, but it’s legal, you may see other people’s code doing it this way round, and you won’t be marked down if you do it this way.

## `float (built-in numeric class)`

There are very few useful methods attached to float (and even fewer on bool or int). Only one is listed here. This is a method not a function, so the syntax uses the ‘.’ after an object of type float.

### `is_integer()`

**Returns:** bool

Returns True if the *float* value is a precise integer value, i.e. will return True on 2.0 but False on 2.1

[Return to the site index](index.md)
