Python Functions
=========================

Note - this page only lists functions - for methods of objects, see the methods section of the [index page](index.md).

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

**len(str OR container) return type: integer [built-in]**
Len gives you the lenth of something. If you give it a string as an argument, it returns the number of characters in the string. This is one of the few string functions which is a normal function, rather than a method of str – so use it like `len("hello")` not `"hello".len()`. If you pass it a container (e.g. a list or dictionary or set) it returns the number of elements in the container.

**min(container) return type: varies [built-in]**
Use on any container (e.g. a list) to find the minimum value. Works on numerical and string elements – for string elements, it will give you the alphabetically first value. Works on dictionaries, but looks at keys not values.

**max(container) return type: varies [built-in]**
Use on any container (e.g. a list) to find the maximum value. Works on numerical and string elements – for string elements, it will give you the alphabetically last value. Works on dictionaries, but looks at keys not values.

**open(filename, mode) return type: file [built-in]**
Tries to open the file with the given filename, in the given mode. Both arguments must be strings. See below for notes on filenames. Mode is a single-character string – it should be “w” for write-mode, “r” for read-mode, or “a” for append mode (append mode is like write mode, but if the file already exists then new data is appended to the end – in write mode it is overwritten). If the file can’t be opened (see below for possible reasons) an exception will be thrown. The open function returns a file object, which is then used for all further file operations – see [file methods](file_methods.md) document.

**ord(string) return type: int [built-in]**
Takes a string of length 1 (i.e. a single-character string) and returns the ASCII code representing it - see e.g. [http://www.asciitable.com/](http://www.asciitable.com/) for a list of codes). Will give an error if the string isn’t length 1.

**print(value) return type: N/A [built-in]**
<br />Outputs (prints) value to the terminal window that the program is running in. value can be a string, a number, or pretty much anything python can evaluate to a string or a number.

**range(start, stop, [step]) return type: weird list-like thing of ints [built-in]**
Generates an iterable/container thing (like a list, but actually not a list) containing integers between start and stop (but not including stop), advancing in step increments. Step is an optional argument – if you omit it, step is 1. So `range(1,5)` gives you `[1,2,3,4]` and `range (1,10,3)` gives you `[1,4,7]`. If you use range with only ONE argument, that argument is treated as a stop value, and start is 1, so `range(5)` gives you `[0,1,2,3,4]`. **IMPORTANT**: range does NOT return a list. Some websites may tell you it does (and it did in older versions of Python), but actually in Python 3 it returns a quirky thing called an "immutable sequence type", which you are probably not going to come across in any other context. This return value *is* an iterable, so the for loop construction works fine with it - e.g. `for i in range(0,5):` – but if you try appending an item to the return value of range it won't work, as it's not actually a list. Luckily it's easy to convert it to a real list – the syntax for this is just `list(range_return_value)`, so e.g. `list_0_to_10 = list(range(0,11))` makes a list of `[0,1,...10]`. 

**str(value) return type: string [built-in]**
<br />Takes a value and tries to convert it into an string. This works on pretty much anything.
