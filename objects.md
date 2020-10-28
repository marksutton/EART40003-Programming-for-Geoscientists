Objects in Python
=================

Python is an Object-Oriented (OO) language, and pretty well everything in Python (including variables which we have thought of as ‘just numbers’) is actually an object. We’ve been calling them variables and thinking of them as just boxes to store things in for (a) simplicity, and (b) compatibility with other languages, in which simple non-object variables normally DO exist. Also, for most of them, most of the time, you don’t have to worry about or care about that fact that they are actually objects. 

Objects can be thought of as data with associated functions that can manipulate that data (called ‘methods’ - see above). See definitions section for more on the object concept, and the related class concept. Most ‘basic’ Python variable data-types don’t have any useful methods (I only give one for `float`, and none for `bool` or `int`) , but `str` (string) objects are the exception – there are a host of string methods, many of which are very handy indeed. Some are given in this reference – others are available in many different online guides. 

To use a method of an object, use the ‘.’ notation – ‘object.method’. So to use the `upper()` method of the a string object, use `my_string.upper()`. This ‘.’ notation is one of the very few bits of syntax that is almost completely standard in computing – it’s used in pretty well all programming languages that include the concept of objects.

<pre>
my_string = "brachiopod".
my_string = my_string.upper()
print(my_string)   # prints ‘BRACHIOPOD’
</pre>

The most common question with objects is ‘What ARE the methods I can use with this object, and what arguments do they take’? The best answer is ‘Google them’ – there are many reference documents out there. Obviously to do this you DO need to make sure that you know what the type (i.e. class name) of the object actually is – to find this, either use a print(type(my_object)) line, or mouseover the name of the object in the Debugger.

NOTE – Python provides an alternative syntax for calling methods – `mystring.upper()` can also be written as `str.upper(mystring)`  (`str` being the name of the string class). This is not encouraged in this course, but it’s legal, you may see other people’s code doing it this way round, and you won’t be marked down if you do it this way.
