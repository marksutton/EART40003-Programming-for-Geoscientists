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

Takes a value and tries to convert it into a number (technically a floating point number - discussed in a later lecture). Normally used to convert a string (e.g. from an `input` function) into a number for calculation. If the value cannot be converted (e.g. `"4.5"` can be converted, `"Forty-two"` cannot), the `float` function will throw an error and stop the program.

## `int(value)`

**Returns:** integer<br>
**Origin:** built-in

Takes a value and tries to convert it into an integer (i.e. a whole number). Normally used to convert a string containing an integer (e.g. from an `input` function) into a number for calculation, but it can also convert a floating-point number such as `2.5` into an integer. When converting a floating-point number, `int` **truncates towards zero**: for example, `int(3.9)` gives `3`, while `int(-5.8)` gives `-5`. This is not the same as rounding to the nearest integer; use `round()` if that is what you need. If a value cannot be converted, `int` throws an error and stops the program. For example, the string `"4"` can be converted, but `"4.5"` and `"Forty-two"` cannot.

[Return to the site index](index.md)
