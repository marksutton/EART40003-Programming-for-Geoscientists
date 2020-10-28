Python Functions
=========================

Note - this page only lists functions - for methods of objects, see the methods section of the [index page](index.md) page.

------------

Functions are given as:

**function_name(arguments) return type: return_type [origin]**

**arguments** is the list of arguments the function expects – the text will tell you what they do. I haven’t always documented all arguments.

**return_type** is the type of value the function returns – in many cases this is a string or a number. Some functions do not return any value – these are given as return type: N/A

**Origin** (my term, not a standard one) is where the function comes from! Some are built-in – others are from a particular library that you will need to import.

--------------------

**abs(number) return type: floating point number or integer [built-in]**
<br />Takes a number (either an int or a float), and returns the same type with the negative sign stripped off (if there was one). Abs is short for ‘absolute’.

**chr(int) return type: string [built-in]**
Takes an integer argument, and returns a single-character string using the ASCII coding system – see e.g. [http://www.asciitable.com/](http://www.asciitable.com/) for a list of codes). Will give an error if the number used as an argument can’t be converted to a valid ASCII code.

**float(value) return type: floating point number [built-in]**
<br />Takes a value and tries to convert it into a number (technically a floating point number – discussed in a later lecture). 
Normally used to convert a string (e.g. from an input function) into a number for calculation. 
If the value cannot be converted (e.g. "4.5" can be converted, "Forty-two" cannot), the float function will throw an error and stop the program.

**input(prompt) return type: string [built-in]**
<br />Provides a simple way to get values from a user while the program is running. Input prints the prompt to the terminal window, then waits for the user to enter some text from the 
keyboard and press enter. 
Prompt can in theory be any type, but should normally be a string (e.g. "enter speed in meters/second "). Input returns the text entered, as a string (always as a string, even 
if only digits are entered). Note that input does not place a space between the printed prompt and the cursor that appears for input, so normally prompt should finish with one or more spaces.

**int(value) return type: integer [built-in]**
<br />Takes a value and tries to convert it into an integer (i.e. a whole number). 
Normally used to convert a string (e.g. from an input function) into a number for calculation, but can also be used to convert a non-integer (floating point) 
number like 2.5 into an integer. Note that the function rounds DOWN towards zero (i.. 3.9 converts to 3, -5.8 converts to -5) 
– if you want to round to the nearest integer instead, add 0.5 before using int. 
If the value cannot be converted (e.g. "4.5" can be converted, "Forty-two" cannot), the int function will throw an error and stop the program.

**len(str) return type: integer [built-in]**
Takes a string as an argument, and returns the number of characters in the string. This is one of the few string functions which is a normal function, rather than a method of str – so use it like `len("hello")` not `"hello".len()`

**ord(string) return type: int [built-in]**
Takes a string of length 1 (i.e. a single-character string) and returns the ASCII code representing it - see e.g. [http://www.asciitable.com/](http://www.asciitable.com/) for a list of codes). Will give an error if the string isn’t length 1.

**print(value) return type: N/A [built-in]**
<br />Outputs (prints) value to the terminal window that the program is running in. value can be a string, a number, or pretty much anything python can evaluate to a string or a number.

**str(value) return type: string [built-in]**
<br />Takes a value and tries to convert it into an string. This works on pretty much anything.
