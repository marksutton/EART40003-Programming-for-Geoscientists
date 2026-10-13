# Definitions

## Argument

See Function.

## Boolean

A Boolean value (named after the mathematician George Boole) is one that can only have one of two values, normally expressed as True or False.

## Breakpoint

See [*Debugger*](#debugger). A point set in a program to force the debugger to stop running at full speed and enter line-at-a-time mode.

## Class

The ‘blueprint’ for an Object. See [*object*](#object) for a proper discussion!

## Comment

Text inserted into a program for the sole-purpose of human-readability. Comments have no effect on the actual running of the program, but are an essential part of programming nonetheless. Turning statements into comments is also a convenient way to temporarily remove a line from your program, without permanently deleting it.

## Condition

Something that a programming language can evaluate to a [*Boolean*](#boolean) value (a True or False), and hence use as the basis of a decision that affects program flow.

## Debugger

A debugger (properly symbolic debugger) is a piece of software that enables a programmer to step through a program line-at-a-time, watching variable values, and following exactly what their program is doing. This is not the only way to debug a program, but is often the easiest way. Debuggers can either be set to step through programs when the user presses a key, or to run the program as normal (full-speed mode) until it reaches a predefined point (a *breakpoint*).

## Exception

An error that occurs during program execution (we say that the exception is *thrown*). In Python, exceptions have a type, and you can check for particular types of error using [*try / except*](exceptions.md)

## Float

a shorthand for [*Floating Point Number*](#floating-point-number).

## Floating point number

The normal method of storing non-integer numbers in a computer. Floating point numbers are stored in a mantissa/exponent format (like 10.43223 x 10<sup>12</sup>, except they use powers of 2 not 10). You don’t need to understand the details of how they are stored, but there are some important consequences of this that you DO need to understand, that arise because they only are approximations to the real numbers they represent. There may be tiny errors in results of calculations arising from this imprecision. Remember in Session 1 when we divided 10 by 3 and got 3.333333333333**5**? That 5 arose from floating point inaccuracies. Precision depends on magnitude, so if (for instance) you add 1 to a huge floating point number (10<sup>100</sup> for instance) you may find that the result is still 10<sup>100</sup> not 10<sup>100</sup>+1 – the precision available may not be enough to tell the difference. You may also find the occasional result like 7.9999999999 from a calculation where you expected 8. Many decimal values cannot be represented exactly as floating-point numbers. For example, in Python `0.1 + 0.2` is not exactly equal to `0.3`. This means you should be very cautious about using `==` or `!=` to compare floating-point results from calculations. Where you need to test whether two floating-point values are effectively equal, compare the difference with a small tolerance instead, for example `abs(a - b) < 0.000001`.

## Function

A separate piece of code that "does something". Functions usually have to be given (passed) one or more values to work on. These passed values are called arguments. Many functions also pass a value back to the main program that launched (called) them. Some functions you will create yourself. Others are built into Python (e.g. the `print` function). Others are written by third parties, and you have to import them. Python function syntax (much the same as in all programming languages) is explained in the Topics section.

## Integer

A whole number. In computing, an integer is a whole number stored in a specific binary format, using a particular number of bits (binary digits). Most languages use a set number of bits for this (32 or 64 typically), which means that integers can ‘overflow’ if they get too large (too large means in the billions at the very least). Python integers never overflow – they expand in size in memory to be as big or as small as they need to be. This makes life easy for us in this course, but if you ever move to another language, remember that integers may have limits.

## Integrated Development Environment (IDE)

A program/application (same thing) designed to bring all the tools you need for programming into one place, and to make the life of a programmer as easy as possible. Thonny is the IDE we are using for this course. Use of an IDE in programming is optional, but it makes your life easier.

## Import

Bring a module (=library) into your program so you can use it.

## Library

See Module. Module is more commonly used in Python, but other languages prefer library. They mean the same thing.

## Linting

Automatic checking of code for "style issues" or errors, underlining them in red. Thonny has a built-in linter, that will underline issues for you. These might be genuine errors, or they might just be ways in which your code isn't quite laid out according to standards. The latter might (will!) all seem like very minor issues, but consistently laid out code really is easier for other people to read, so try to follow these rules.

## Method

a function provided as part of a class, intended to work on the data of that class. For instance, capitalize() is a method of the Python *str* class – it returns a version of the string with an initial capital letter.

## Module

A pre-written set of functions for some particular purpose or set of purposes that you can bring into your program (import). There are many modules for Python already installed on your computer.

## Nesting

Putting a program structure inside another program structure. Pretty well anything can be nested in programming, including function calls, if statements, loops etc. Nesting takes two forms in Python. Nesting within expressions - e.g. `float(input("hello"))` - consists of brackets within brackets (innermost always happens first). Nesting of control structures (`if`, `while` etc.) is done using indentation. Most languages encourage this indentation for readability, but in Python it is mandatory.

## Object

An instance of a *Class*. The distinction between objects and classes in Python can be confusing and is a little blurry because of some esoteric aspects of the language design (if you Google this you will find some people telling you that classes are also objects in Python, which though true is very unhelpful). For the purposes of this course, think of a *class* as a particular type of data together with some functions designed to work on that data. The functions are properly called *methods* when they are attached to a class, but they are still functions – they use brackets, have arguments, and return values. The *str* class in Python is a good example of a class – it stores text (obviously), and provides many methods that do things to that text (capitalize(), upper(), lower(), etc.). An object is a particular instance of that class, so when you say my_string = “hello”, you have made an object – an instance of the str class. Classes can thus be thought of as blueprints for objects. See [Objects in Python](objects.md) for more on objects in Python.

## Pass

See Function.

## Program

A series of commands to a computer used to perform some particular task, i.e. a piece of software. Application or App mean essentially the same thing. Programs are created as text using a programming language, and then translated by other programs into the machine language that the computer actually understands (you never really see this stage). Note - the standard is American spelling here, so it's *program* not *programme*.

## Programming language

A standardised set of rules for how you should phrase commands to a computer that make up a program. Python is a programming language - other common ones include C, C++, Java, but there are many hundreds in existence. Some are specialised for particular tasks - others (like Python) are general-purpose.

## Python

A general-purpose programming language that we are using in this course.

## Return value

See Function.

## Statement

A line of a program that does something. Some statements will be function calls (e.g. a `print` line). Others may assign values to variables, start or end control structures like loops, or more. In Python you only have one statement per line.*

*Technical note: actually there is a way to have more than one statement per line in Python, but it is not considered good Python style. For the purposes of this course, the one-statement-per-line rule holds.*

## String

Text (called a string as text is a string of characters).

## Syntax Error

A programming error that is detected before the program runs… things like missing brackets or colons, or other unambiguously illegal code.

## Type

(of variables or other data). The type of information stored, and/or the coding scheme used to store them. Understanding what *type* your variables are is critical to understanding what is going on in a program. Simple variable types in Python are int (short for *Integer*), float (short for *Floating point number*), bool (short for *Boolean*, i.e. a True/False variable) and str (string).

## Variable

A variable is best thought of as a box in the computer's memory which can store some value for you to do something with later. Variables have names which the programmer assigns - **these should be chosen to aid readability of the program**, i.e. they should give at least a hint as to what the value is used for (e.g. `age_in_years`, not just `a`). Variables have a "type" - the sort of value they hold (e.g. a string or a number - it's actually much more complex than that, but that will do for now). Once you put a value into a variable, it stays there until the program finishes, or until you put a new value into it.

[Return to the site index](index.md)
