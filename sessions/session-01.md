---
course: EART40003
course_title: Programming for Geoscientists
session: 1
year: 2026
author_short: MDS
title: "Session 1: Reference"
header_title: "Session 1 - Reference"
---

<!-- handout-only:start -->

I'll generate one of these reference documents each session, containing definitions for terms I introduce, and formal explanations of the Python we introduce too. There may well be more detail here than in the PowerPoint or examples. There's also a combined reference site, with all these documents integrated together - <https://marksutton.github.io/EART40003-Programming-for-Geoscientists>. This covers the whole course, so will have plenty of things we've not covered at this stage.

<!-- handout-only:end -->

# Definitions

### Argument

See Function.

### Comment

Text inserted into a program for the sole-purpose of human-readability. Comments have no effect on the actual running of the program, but are an essential part of programming nonetheless. Turning statements into comments is also a convenient way to temporarily remove a line from your program, without permanently deleting it.

### Function

A separate piece of code that "does something". Functions usually have to be given (passed) one or more values to work on. These passed values are called arguments. Many functions also pass a value back to the main program that launched (called) them. Some functions you will create yourself. Others are built into Python (e.g. the `print` function). Others are written by third parties, and you have to import them. Python function syntax (much the same as in all programming languages) is explained in the Topics section.

### Integrated Development Environment (IDE)

A program/application (same thing) designed to bring all the tools you need for programming into one place, and to make the life of a programmer as easy as possible. Thonny is the IDE we are using for this course. Use of an IDE in programming is optional, but it makes your life easier.

### Import

Bring a module (=library) into your program so you can use it.

### Library

See Module. Module is more commonly used in Python, but other languages prefer library. They mean the same thing.

### Linting

Automatic checking of code for "style issues" or errors, underlining them in red. Thonny has a built-in linter, that will underline issues for you. These might be genuine errors, or they might just be ways in which your code isn't quite laid out according to standards. The latter might (will!) all seem like very minor issues, but consistently laid out code really is easier for other people to read, so try to follow these rules.

### Module

A pre-written set of functions for some particular purpose or set of purposes that you can bring into your program (import). There are many modules for Python already installed on your computer.

### Pass

See Function.

### Program

A series of commands to a computer used to perform some particular task, i.e. a piece of software. Application or App mean essentially the same thing. Programs are created as text using a programming language, and then translated by other programs into the machine language that the computer actually understands (you never really see this stage). Note - the standard is American spelling here, so it's *program* not *programme*.

### Programming language

A standardised set of rules for how you should phrase commands to a computer that make up a program. Python is a programming language - other common ones include C, C++, Java, but there are many hundreds in existence. Some are specialised for particular tasks - others (like Python) are general-purpose.

### Python

A general-purpose programming language that we are using in this course.

### Return value

See Function.

### Statement

A line of a program that does something. Some statements will be function calls (e.g. a `print` line). Others may assign values to variables, start or end control structures like loops, or more. In Python you only have one statement per line.*

*Technical note: actually there is a way to have more than one statement per line in Python, but it is not considered good Python style. For the purposes of this course, the one-statement-per-line rule holds.*

### String

Text (called a string as text is a string of characters).

### Variable

A variable is best thought of as a box in the computer's memory which can store some value for you to do something with later. Variables have names which the programmer assigns - **these should be chosen to aid readability of the program**, i.e. they should give at least a hint as to what the value is used for (e.g. `age_in_years`, not just `a`). Variables have a "type" - the sort of value they hold (e.g. a string or a number - it's actually much more complex than that, but that will do for now). Once you put a value into a variable, it stays there until the program finishes, or until you put a new value into it.

# Functions

These are given as:

```text
function_name(arguments) return type: return_type [origin]
```

`arguments` is the list of arguments the function expects - the text will tell you what they do. I haven't always documented all arguments.

`return_type` is the type of value the function returns - in many cases this is a string or a number. Some functions do not return any value - these are given as `return type: N/A`.

`origin` (my term, not a standard one) is where the function comes from! Some are built-in - others are from a particular library that you will need to import.

### `print(value)`

**Returns:** N/A  
**Origin:** built-in

Outputs (prints) `value` to the terminal window that the program is running in. `value` can be a string, a number, or pretty much anything Python can evaluate to a string or a number.

### `input(prompt)`

**Returns:** string  
**Origin:** built-in

Provides a simple way to get values from a user while the program is running. `input` prints the `prompt` to the terminal window, then waits for the user to enter some text from the keyboard and press enter. `prompt` can in theory be any type, but should normally be a string (e.g. `"enter speed in meters/second "`). `input` returns the text entered, as a string (always as a string, even if only digits are entered). Note that `input` does not place a space between the printed prompt and the cursor that appears for input, so normally `prompt` should finish with one or more spaces.

### `float(value)`

**Returns:** floating point number  
**Origin:** built-in

Takes a value and tries to convert it into a number (technically a floating point number - discussed in a later lecture). Normally used to convert a string (e.g. from an `input` function) into a number for calculation. If the value cannot be converted (e.g. `"4.5"` can be converted, `"Forty-two"` cannot), the `float` function will throw an error and stop the program.

# Topics

## Operators

Operators are symbols used to do things to values or variables, e.g. to add them.

### `=` operator

Used to assign values to variables, as a statement in its own right. There should always be exactly one variable-name to the left of an `=` operator, but to the right can be anything that Python can evaluate to a value (another variable, a number, a calculation, a function call, or combinations of these). If the variable to the left of the `=` does not yet exist, it is created automatically.

```python
my_variable = 10   # create 'my_variable' (if it doesn't already exist) and set it to 10
a_string = "ten"   # assign the string "ten" to variable a_string
my_v = 7*3         # do a calculation, assign result to my_v
my_v = v1 + 2      # add 2 to variable v1, assign result to my_v
a = float("10")+1  # convert string "10" to a value, add 1, assign result to a
b = b + 1          # increase value of variable b by 1
b = (c*(a**z))/10.2   # do complex calculation, assign result to b
```

```python-invalid
50 = my_variable   # illegal - needs a variable to the left of the =
```

### `+` operator

Adds two numbers together. If the values either side of the `+` are strings, it joins them together instead.

```python
c = 10 + 2   # Add 10 and 2, put result (12) into variable c
d = x + 6    # If x is a number, value of x + 6 assigned to d. If x is a string this
             # will give an error (strings can only be added to other strings)
e = a + "?"  # If a is a string, put a ? on the end of it and assign that to variable e.
             # If a is a number this will give an error for the same reason as above.
```

### `-` operator

Performs subtraction. Can only be used on numbers (not strings).

```python
c = e - 2      # Subtract 2 from the value in variable e, assign result to variable c
```

```python-invalid
d = "ten" - 3  # ILLEGAL - can't subtract from a string
```

### `*` operator

Performs multiplication. Can only be used on numbers (not strings).

```python
print(e * 2)    # Multiply the value in variable e by 2, print it
d = 200 * b     # Multiply b by 200, put result in d
```

### `/` operator

Performs division. Can only be used on numbers (not strings). Attempting to divide by 0 will generate an error.

```python
print(1 / 2)    # Calculate 1/2, print the result (0.5)
v = x / c       # Divide values of x by value of c, put result in v
```

```python-invalid
v = x / 0       # ILLEGAL - you can't divide by 0.
```

### `**` operator

Raise a number to the power of another number. You can use negative and non-integer powers.

```python
print(10 ** 2)     # prints 10 squared (100)
sqrt_a = a ** 0.5  # Raise a to the power of 0.5 (= square root), put result in sqrt_a
a = b ** c         # work out b to the power of c, put result in a
```

### `%` operator

For numbers, this performs a modulus calculation (i.e. works out the remainder of a division).

```python
print(15 % 6)      # print the remainder when dividing 15 by 6 (3)
a = b % c          # calculate the remainder from dividing b by c, assign it to a.
                   # this assumes b and c are both numbers
```

## Variable names

Variable names in Python can be any length and can consist of uppercase and lowercase letters (`A-Z`, `a-z`), digits (`0-9`), and the underscore character (`_`). Most important, note that **they cannot include spaces!** An additional restriction is that, although a variable name can contain digits, **the first character of a variable name cannot be a digit**. There are also some reserved Python keywords which cannot be used as variable names, including `False`, `True`, `None`, `if`, `else`, `for`, `while`, `def`, `class`, `return` and `import`.

Variable names are **case sensitive** - so `MyVariable` is NOT the same variable as `Myvariable`. This is a common source of errors, so look out for it.

Variable names should be meaningful - they should help someone reading your code understand what the variable is used for. Avoid single-letter variables (I've used some in examples here, but just to save space). Don't worry about how long it takes to type longer names - Thonny has an auto-fill feature that will bring them up for you if you start typing - but a good maximum length though would be ~20 characters. Where variable names incorporate multiple words (recall that you can't use spaces), avoid just running them together (so `accelerationduetogravity` is bad - it's hard to read). In these cases you can use either:

- `accelerationDueToGravity` (this is called Camel Case)
- `AccelerationDueToGravity` (this is called Pascal Case)
- `acceleration_due_to_gravity` (using underscores for spaces - this is called snake case)

It doesn't really matter which of these you use, although the last one (snake case) is the most commonly used in Python, and is what I will use in my examples. What DOES matter though is that you are consistent.

## String syntax

In programs, you should surround text that you want to be treated as a string with either single or double quotes (`'` or `"` - the latter is the shift-2 character, not two single quotes next to each other). If you don't do this, Python will try to treat the text as a variable name or a statement, and you will probably get an error.

To include a newline in a string (the equivalent of hitting return) you have two options - you can use `\n` (which prints as a line-break) or you can surround your string with triple double quotes, then use actual line breaks. So both of the following examples:

```python
print("new\nline")
print("""new
line""")
```

will print as:

```text
new
line
```

## F strings

'F strings' (properly called 'formatted string literals') provide a way to insert values (normally from variables) into a string. This is a very common thing to want to do! There are at least three other ways to do this in Python, and if you look at code available online you may see these other approaches being used. The 'f string' approach though is the most modern and probably the most convenient, so you should use it in this course.

In their simplest form, you use f strings by just inserting variable names into strings inside braces `{ }`, and prefixing the `"` at the start of the string with an `f`. There are some complexities though - these are best explained by examples.

> **Example setup:** In these examples, `my_variable` has the floating point value `4.29`, `my_string` is `"hello"`, and `other_variable` has the integer value `8`. Output / comments are given below in italics.

```python
print(f"Result is {my_variable}")
```

*Prints Result is 4.29*

```python
print(f"{my_string}, the result is {my_variable}")
```

*Prints hello, the result is 4.29 (you can have multiple variables in braces, and can include strings)*

```python
print(f"Result is {my_variable + 2.1}")
```

*Prints Result is 6.39 (you can do calculations inside the braces!)*

```python
print(f"Found {other_variable} open braces {{")
```

*Prints Found 8 open braces { (to use a { or } in an f string you have to double it)*

```python
new_string = f"Value is {my_variable}"
```

*Sets `new_string` to "Value is 4.29" (you can use f strings outside of print functions)*

```python
print(f"Result to one d.p. is {my_variable:.1f}")
```

*Prints Result to one d.p. is 4.3 (the `:.1f` specifies number of decimal places - very useful!)*

```python
print(f"Result to four d.ps is {my_variable:.4f}")
```

*Prints Result to four d.ps is 4.2900 (and again, four decimal places this time)*

```python
print(f"Result is {other_variable:02}")
```

*Prints Result is 08 (`02` means use two columns, padding with leading zeros)*

```python
print(f"Result is {other_variable:3}")
```

*Prints Result is   8 (`3` means use three columns, padding with spaces)*

```python
print(f"Result is {my_variable:07.3f}")
```

*Prints Result is 004.290 (you can combine padding with decimal places - but padding counts total characters)*

There IS more to the complex world of string formatting, but the examples above should cover most of what you want to do. See e.g. <https://www.w3schools.com/python/python_string_formatting.asp> for more details if you need them.
