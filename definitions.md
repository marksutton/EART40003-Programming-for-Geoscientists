Definitions
-----------

**Argument**: See Function

**Boolean**: A Boolean value (named after the mathematician George Bool) is one that can only have one of two values, normally expressed as True or False.

**Breakpoint**: See Debugger. A point set in a program to force the debugger to stop running at full speed and enter line-at-a-time mode.

**Comment**: Text inserted into a program for the sole-purpose of human-readability. Comments have no effect on the actual running of the program, but are an essential part of programming nonetheless. Turning statements into comments is also a convenient way to temporarily remove a line from your program, without permanently deleting it.

**Condition**: Something that a programming language can evaluate to a Boolean value (a True or False), and hence use as the basis of a decision that affects program flow.

**Debugger**: A debugger (properly symbolic debugger) is a piece of software that enables a programmer to step through a program line-at-a-time, watching variable values, and following exactly what their program is doing. This is not the only way to debug a program, but is often the easiest way. Debuggers can either be set to set through programs when the user presses a key, or to run the program as normal (full-speed mode) until it reaches a predefined point (a breakpoint). The debugger built into VSCode always starts in full-speed mode, but setting a breakpoint on the first line will force it to stop and enter line-at-a-time mode straight away.

**Flake8**: The linting system for python that we are using in this course.

**Function**: a separate piece of code that ‘does something’. Functions usually have to be given (passed) one or more values to work on. These passed values are called arguments. Many functions also pass a value back to the main program than launched (called) them. Some functions you will create yourself. Others are built into python (e.g. the print function). Others are written by third parties, and you have import them. Python function syntax (much the same as in all programming languages) is explained in the Syntax section.

**Integrated Development Environment (IDE)**: A program/application (same thing) designed to bring all the tools you need for programming into one place, and to make the life of a programmer as easy as possible. VScode is the IDE we are using for this course. Use of an IDE in programming is optional.

**Import**: Bring a library into your program so you can use it.

**Library**: A pre-written set of functions for some particular purpose or set of purposes that you can bring into your program (import). There are many many libraries for python already installed on your computer.

**Linting**: Automatic checking of code for ‘style issues’ or errors, underlining them in red. Flake8 is the linter used in this course. Linting will not only flag up mistakes, but will also flag up ways in which your code isn’t quite laid out according to standards. These might (will!) all seem like very minor issues, but consistently laid out code really is easier for other people to read, so try to follow these rules.

**Nesting**: Putting a program structure inside another program structure. Pretty well anything can be nested in programming, including function calls, if statements, loops etc. Nesting takes two forms in Python. Nesting within expressions - e.g. `float(input("hello"))` – consists of brackets within brackets (innermost always happens first). Nesting of control structures (if, while etc.) is done using indentation. Most languages encourage this indentation for readability, but in in Python it is mandatory.

**Pass**: See Function

**Program**: A series of commands to a computer used to perform some particular task, i.e. a piece of software. Application or App mean essentially the same thing. Programs are created as text using a programming language, and then translated by other programs into the machine language that the computer actually understands (you never really see this stage). Note – standard is American spelling here, so program not programme.

**Programming language**: A standardised set of rules for how you should phrase commands to a computer that make up a program. Python is a programming language – other common ones include C, C++, Java, but there are many hundreds in existence. Some are specialised for particular tasks – others (like Python) are general-purpose.

**Python**: A general-purpose programming language that we are using in this course.

**Return value**: See Function

**Statement**: A line of a program that does something. Some statements will be function calls (e.g. a print line). Others may assign values to variables, start or end control structures like loops, or more. In python you only have one statement per line, but some other languages complicate this.

**String**: text (called a string as text is a string of characters).

**Variable**: A variable is best thought of as a box in the computer’s memory which can store some value for you to do something with later. Variables have names which the programmer assigns – these should be chosen to aid readability of the program, i.e. they should give at least a hint as to what the value is used for (e.g. age_in_years, not just a). Variables have a ‘type’ – the sort of value they hold (e.g. a string or a number – it’s actually much more complex than that, but that will do for now). Once you put a value into a variable, it stays there until the program finishes, or until you put a new value into it.
Visual Studio Code / VSCode: The IDE used in this module

