---
course: EART40003
course_title: Programming for Geoscientists
session: 3
year: 2026
author_short: MDS
title: "Session 3: Reference"
subtitle: "Pre-reading from Session 2"
---

# Definitions

### Class

The ‘blueprint’ for an Object. See *object* for a proper discussion!

### Exception

An error that occurs during program execution (we say that the exception is *thrown*). In Python, exceptions have a type, and you can check for particular types of error using *try / except* (see syntax section)

### Float

a shorthand for *Floating Point Number*.

### Floating point number

The normal method of storing non-integer numbers in a computer. Floating point numbers are stored in a mantissa/exponent format (like 10.43223 x 10<sup>12</sup>, except they use powers of 2 not 10). You don’t need to understand the details of how they are stored, but there are some important consequences of this that you DO need to understand, that arise because they only are approximations to the real numbers they represent. There may be tiny errors in results of calculations arising from this imprecision. Remember in Session 1 when we divided 10 by 3 and got 3.333333333333**5**? That 5 arose from floating point inaccuracies. Precision depends on magnitude, so if (for instance) you add 1 to a huge floating point number (10<sup>100</sup> for instance) you may find that the result is still 10<sup>100</sup> not 10<sup>100</sup>+1 – the precision available may not be enough to tell the difference. You may also find the occasional result like 7.9999999999 from a calculation where you expected 8. Many decimal values cannot be represented exactly as floating-point numbers. For example, in Python `0.1 + 0.2` is not exactly equal to `0.3`. This means you should be very cautious about using `==` or `!=` to compare floating-point results from calculations. Where you need to test whether two floating-point values are effectively equal, compare the difference with a small tolerance instead, for example `abs(a - b) < 0.000001`.

### Integer

A whole number. In computing, an integer is a whole number stored in a specific binary format, using a particular number of bits (binary digits). Most languages use a set number of bits for this (32 or 64 typically), which means that integers can ‘overflow’ if they get too large (too large means in the billions at the very least). Python integers never overflow – they expand in size in memory to be as big or as small as they need to be. This makes life easy for us in this course, but if you ever move to another language, remember that integers may have limits.

### Method

a function provided as part of a class, intended to work on the data of that class. For instance, capitalize() is a method of the Python *str* class – it returns a version of the string with an initial capital letter.

### Object

An instance of a *Class*. The distinction between objects and classes in Python can be confusing and is a little blurry because of some esoteric aspects of the language design (if you Google this you will find some people telling you that classes are also objects in Python, which though true is very unhelpful). For the purposes of this course, think of a *class* as a particular type of data together with some functions designed to work on that data. The functions are properly called *methods* when they are attached to a class, but they are still functions – they use brackets, have arguments, and return values. The *str* class in Python is a good example of a class – it stores text (obviously), and provides many methods that do things to that text (capitalize(), upper(), lower(), etc.). An object is a particular instance of that class, so when you say my_string = “hello”, you have made an object – an instance of the str class. Classes can thus be thought of as blueprints for objects. See objects under syntax for more on objects in Python.

### Syntax Error

A programming error that is detected before the program runs… things like missing brackets or colons, or other unambiguously illegal code.

### Type

(of variables or other data). The type of information stored, and/or the coding scheme used to store them. Understanding what *type* your variables are is critical to understanding what is going on in a program. Simple variable types in Python are int (short for *Integer*), float (short for *Floating point number*), bool (short for *Boolean*, i.e. a True/False variable) and str (string).

# Functions

### `abs(number)`

**Returns:** number  
**Origin:** built-in  

Takes a number (either an int or a float), and returns the same type with the negative sign stripped off (if there was one). Abs is short for ‘absolute’.

### `chr(int)`

**Returns:** string  
**Origin:** built-in  

Takes an integer argument, and returns a single-character string using the ASCII coding system – see e.g. <http://www.asciitable.com/> for a list of codes). Will give an error if the number used as an argument can’t be converted to a valid ASCII code.

### `len(str)`

**Returns:** int  
**Origin:** built-in  

Takes a string as an argument, and returns the number of characters in the string. This is one of the few string functions which is a normal function, rather than a method of str – so use it like **len(“hello”)** not **“hello”.len()**

### `ord(string)`

**Returns:** int  
**Origin:** built-in  

Takes a string of length 1 (i.e. a single-character string) and returns the ASCII code representing it – see e.g. <http://www.asciitable.com/> for a list of codes). Will give an error if the string isn’t length 1.

### `str(value)`

**Returns:** string  
**Origin:** built-in  

Takes a value and tries to convert it into a string. Will work with most variable types

# Methods

### `float (built-in numeric class)`

There are very few useful methods attached to float (and even fewer on bool or int). Only one is listed here. This is a method not a function, so the syntax uses the ‘.’ after an object of type float.

#### `is_integer()`

**Returns:** bool  

Returns True if the *float* value is a precise integer value, i.e. will return True on 2.0 but False on 2.1

### `str (built-in string class)`

These are methods not functions, so the syntax uses the ‘.’ after an object of type str. For example, use **"hello".capitalize()** not **capitalize("hello")**. There are many string methods – not all are listed here, and for some that are there are optional extra arguments that I do not document here.

#### `capitalize()`

**Returns:** str  

Returns a version of the string with the initial letter capitalized.

#### `count(substring)`

**Returns:** int  

Counts how many times ‘substring’ occurs in the string, then returns this count (which may be 0) as an integer.

#### `find(substring)`

**Returns:** int  

Returns the index (position) of the first occurrence of ‘substring’ occurs in the string. If substring isn’t found, it returns -1.

#### `isalpha()`

**Returns:** bool  

Returns True if all characters in the string are letters, otherwise returns False

#### `isnumeric()`

**Returns:** bool  

Returns True if all characters in the string are digits, otherwise returns False

#### `lower()`

**Returns:** str  

Returns a copy of the string with all characters converted to lowercase.

#### `replace(oldtext, newtext)`

**Returns:** str  

Returns a copy of the string in which all occurrences of the text *oldtext* are replaced with *newtext*.

#### `strip()`

**Returns:** str  

Returns a copy of the string with any whitespace characters (spaces, tabs, newlines) removed from both the start and end

#### `upper()`

**Returns:** str  

Returns a copy of the string with all characters converted to uppercase.

# Topics

## Objects in Python

Python is an Object-Oriented (OO) language, and pretty well everything in Python (including variables which we have thought of as ‘just numbers’) is actually an object. We’ve been calling them variables and thinking of them as just boxes to store things in for (a) simplicity, and (b) compatibility with other languages, in which simple non-object variables normally DO exist. Also, for most of them, most of the time, you don’t have to worry about or care about that fact that they are actually objects.

Objects can be thought of as data with associated functions that can manipulate that data (called ‘methods’ - see above). See definitions section for more on the object concept, and the related *class* concept. Most ‘basic’ Python variable data-types don’t have many methods that we need in this course (I only give one for *float*, and none for bool or int), but *str* (string) objects are the exception – there are a host of string methods, many of which are very handy indeed. Some are given in this reference – others are available in many different online guides.

To use a method of an object, use the ‘.’ notation – ‘object.method’. So to use the upper() method of the a string object, use **my_string.upper()**. This ‘.’ notation is one of the very few bits of syntax that is almost completely standard in computing – it’s used in pretty well all programming languages that include the concept of objects.

```python
my_string = "brachiopod"
my_string = my_string.upper()
print(my_string)   # prints ‘BRACHIOPOD’
```

The most common question with objects is ‘What ARE the methods I can use with this object, and what arguments do they take’? The best answer is ‘Google them’ – there are many reference documents out there. Obviously to do this you DO need to make sure that you know what the type (i.e. class name) of the object actually is – to find this, look in the Thonny variables window, or for more obscure types not listed there, use `print(type(my_object))`.

NOTE – Python provides an alternative syntax for calling methods – **mystring.upper()** can also be written as **str.upper(mystring)**  (str being the name of the string class). This is not encouraged in this course, but it’s legal, you may see other people’s code doing it this way round, and you won’t be marked down if you do it this way.

## String slicing syntax

Python provides a flexible and easy-to-use way to extract bits of strings (compared to many other languages, which often make heavy-going of this). This involves appending the string with [x:y], where x is the first character you want, and y is the first character that you don’t want – so if you want characters 3-7, x will be 3, y will be 8. If you only want one character at position x, you can write [x]. There are a few shortcuts and conventions to this, which are best explained by example (so see examples below). Counting starts at 0 (so “hello”[1] is “e” not “h”). You can put the [] after a string value in quotes, or a string variable, or even a string expression – so **(string1 + string2)[10:20]** is legal Python – meaning join string2 to string1, then give me the string between character 10 and 20 of the combined string. Note the brackets – this makes sure that the joining is done before the slicing (just like brackets in numerical expressions). Some examples of string-slicing:

| Expression | Meaning – Value | Expression | Meaning - Value |
| --- | --- | --- | --- |
| `"slicing"[0]` | Character 0 - `"s"` | `"slicing"[4:]` | Character 4 to end – `"ing"` |
| `"slicing"[1:3]` | Characters 1-2 – `"li"` | `"slicing"[-4:-2]` | Characters 4<sup>th</sup> from end to 3<sup>rd</sup> from end – `"ci"` |
| `"slicing"[:5]` | Start to character 4 – `"slici"` | `"slicing"[-4:]` | Characters 4<sup>th</sup> from end to end (i.e. last 4 characters) – `"cing"` |

## try / except

Exceptions are run-time errors like divide by zero, failed conversions from strings to numbers, etc. You don’t want these appearing when a program runs if you can avoid it. You can either write code that checks for problems before it does the step that throws the error (e.g. check that a string only includes digits before trying to convert it), or you can let the exception occur and *catch* it – write code that intercepts it and does something more elegant than crashing. The syntax is:

::: syntax-template

try:

    [lines to execute]

except ExceptionName1:

    [lines to execute if ExceptionName1 happened]

except ExceptionName2:

    [lines to execute if ExceptionName2 happened]

…

except Exception:

    [lines to execute if there was an exception not caught above]

else:

    [lines to execute if there was no exception at all]

:::

‘else’ is optional, and multiple except blocks are also optional – but if you have a ‘try’ you have to have at least one ‘except’.

> **Best practice:** When catching exceptions, mention specific exceptions whenever possible instead of using a ‘bare except’ (i.e just `except:`). A bare except will catch `SystemExit` and `KeyboardInterrupt` exceptions, making it harder to interrupt a program with Control-C, and can disguise other problems. If you want to catch all exceptions that signal program errors, use `except Exception:`

Exception names are not going to be guessable – they are things like ZeroDivisionError, and you need to get them exactly right. They can be looked up, but it’s almost always simpler to simply do something that generates the error, then see what it is! For instance…

```python
a = "ten"
a = float(a)
```

Will generate an exception, as the float function won’t like the string **"ten".** If you run this, you get…

```text
Traceback (most recent call last):
  File "d:/Teaching/Programming/test.py", line 2, in <module>
    a = float(a)
ValueError: could not convert string to float: 'ten'
```

… which tells you that this exception is called ValueError.

# Exercises

## Exercise: What would each of these code snippets print?

| Code | Prints? |
| --- | --- |
| `"Ganymede"[7]` |  |
| `s = "Ganymede"`<br>`print(len(s))` |  |
| `s = "Mercury"`<br>`print(s[:3])` |  |
| `s = "Jupiter"`<br>`s2 = s[3:].upper()`<br>`print(s2)` |  |
| `print(("Moon"+"Mars")[2:].count("o"))` |  |
| `print("Jupiter"[4].isnumeric())` |  |
| `s = "Hello"`<br>`s2 = "!!!"`<br>`print((s.replace("l",s2[-2:])).count("!"))` |  |
