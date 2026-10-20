# Functions

These are given as:

`function_name(arguments)`

**Returns:** return type<br>
**Origin:** origin

`arguments` is the list of arguments the function expects - the text will tell you what they do. I haven't always documented all arguments.

`Returns` describes the type of value the function returns - in many cases this is a string or a number. Some functions do not return any value - these are given as **Returns:** N/A.

`origin` (my term, not a standard one) is where the function comes from! Some are built-in - others are from a particular library that you will need to import.

## `print(value)`

**Returns:** N/A<br>
**Origin:** built-in

Outputs (prints) `value` to the terminal window that the program is running in. `value` can be a string, a number, or pretty much anything Python can evaluate to a string or a number.

## `input(prompt)`

**Returns:** string<br>
**Origin:** built-in

Provides a simple way to get values from a user while the program is running. `input` prints the `prompt` to the terminal window, then waits for the user to enter some text from the keyboard and press enter. `prompt` can in theory be any type, but should normally be a string (e.g. `"enter speed in meters/second "`). `input` returns the text entered, as a string (always as a string, even if only digits are entered). Note that `input` does not place a space between the printed prompt and the cursor that appears for input, so normally `prompt` should finish with one or more spaces.

## `float(value)`

**Returns:** floating point number<br>
**Origin:** built-in

Takes a value and tries to convert it into a number (technically a [floating point number](definitions.md#floating-point-number)). Normally used to convert a string (e.g. from an `input` function) into a number for calculation. If the value cannot be converted (e.g. `"4.5"` can be converted, `"Forty-two"` cannot), the `float` function will throw an error and stop the program.

## `int(value)`

**Returns:** integer<br>
**Origin:** built-in

Takes a value and tries to convert it into an integer (i.e. a whole number). Normally used to convert a string containing an integer (e.g. from an `input` function) into a number for calculation, but it can also convert a floating-point number such as `2.5` into an integer. When converting a floating-point number, `int` **truncates towards zero**: for example, `int(3.9)` gives `3`, while `int(-5.8)` gives `-5`. This is not the same as rounding to the nearest integer; use `round()` if that is what you need. If a value cannot be converted, `int` throws an error and stops the program. For example, the string `"4"` can be converted, but `"4.5"` and `"Forty-two"` cannot.

## `abs(number)`

**Returns:** number<br>
**Origin:** built-in

Takes a number (either an int or a float), and returns the same type with the negative sign stripped off (if there was one). Abs is short for ‘absolute’.

## `chr(int)`

**Returns:** string<br>
**Origin:** built-in

Takes an integer argument, and returns a single-character string using the ASCII coding system – see e.g. <http://www.asciitable.com/> for a list of codes). Will give an error if the number used as an argument can’t be converted to a valid ASCII code.

<a id="lenstr"></a>

## `len(container)`

**Returns:** int<br>
**Origin:** built-in

Takes a string as an argument, and returns the number of characters in the string. This is one of the few string functions which is a normal function, rather than a method of str – so use it like **len(“hello”)** not **“hello”.len()**

The len function, which we have seen used on strings, also works on containers such as lists – it returns the number of elements.

## `ord(string)`

**Returns:** int<br>
**Origin:** built-in

Takes a string of length 1 (i.e. a single-character string) and returns the ASCII code representing it – see e.g. <http://www.asciitable.com/> for a list of codes). Will give an error if the string isn’t length 1.

## `str(value)`

**Returns:** string<br>
**Origin:** built-in

Takes a value and tries to convert it into a string. Will work with most variable types

## `min(container)`

**Returns:** varies<br>
**Origin:** built-in

Use on any container (e.g. a list) to find the minimum value. Works on numerical and string elements – for string elements, it will give you the alphabetically first value.

## `max(container)`

**Returns:** varies<br>
**Origin:** built-in

Use on any container (e.g. a list) to find the maximum value. Works on numerical and string elements – for string elements, it will give you the alphabetically last value.

## `range(start, stop, [step])`

**Returns:** weird list-like thing of ints<br>
**Origin:** built-in

Generates an iterable/container thing (like a list, but actually not a list) containing integers between *start* and *stop* (but not including stop), advancing in *step* increments. *Step* is an optional argument – if you omit it, *step* is 1. So **range(1,5)** gives you [**1,2,3,4]** and **range (1,10,3)** gives you **[1,4,7]**. If you use range with only ONE argument, that argument is treated as a stop value and the implicit start is 0, so **range(5)** represents the values **[0,1,2,3,4]**. IMPORTANT: *range* does NOT return a list. Some websites may tell you it does (and it did in older versions of Python), but actually in Python 3 it returns a quirky thing called an "immutable sequence type", which you are probably not going to come across in any other context. It’s a bit like a list – but not quite a list. This return value *is* an 'iterable' at least, so the for loop construction works fine with it - e.g. **for i in range(0,5):**. It is legal to print a range object, but this does not print its contained values as though it were a list: in the course Python 3.14 environment, **print(range(5))** displays a representation such as **range(5)**. If you want the actual values as a list, use **list(range(...))**, so e.g. **list_0_to_10 = list(range(0,11))** works.

## `sum(container)`

**Returns:** number<br>
**Origin:** built-in

Use on any container (e.g. a list) to find the sum of all values in the container. Works on numerical but not string elements.

[Return to the site index](index.md)
