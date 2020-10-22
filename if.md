if / elif / else
----------------

In Python, these three keywords provide all conditional program flow functionality. 
They are used together, in an **if block**. An if block begins with an if statement, 
followed by indented lines of code to be executed if the condition is True. 
Optionally, it can also have one or more elif statements (elif is short for else if, though if you type 'else if' Python won’t understand it) 
plus associated indented lines of code. These are used to catch alternative conditions, 
Finally, optionally again, you can have one else statement and associated code, to catch any cases not caught already. 
Crucially, at most only ONE block of indented code is executed each time the program runs through an entire if/elif/else block. See [conditions](conditions.md) for how to construct a condition.
<pre>
if condition1:
    Code to execute if condition1 was True (can be as many lines as needed)
elif condition2:    [elif blocks are optional]		
    Code to execute if condition2 was True and condition1 was false (can be as many lines as needed)
elif condition3:    [elif blocks are optional]		
    Code to execute if condition3 was True and both condition1 and condition 2 were false
…. [as many elif blocks as you like]
else:                      [else block is optional]
    Code to execute if none of the if or elif conditions were True
</pre>

Common errors to watch out for with if’s:
---------------------
* Frgetting the colon (‘:’) at the end of the if / elif / else line. This is required.
* Forgetting to indent. Python absolutely needs indents to tell it which statements are in which block
* Unreachable blocks. For instance, if your ‘if’ condition is ‘a > 5’, an elif block with a condition of ‘a > 10’ will never be executed – if a > 10 it’s also > 5, so the initial if block will run, not the elif block
* Condition errors – see conditions section.

<pre>
# example 1 – simple if check to warn user if a value is too big for a calculation to be reliable

if a > 1000:
    print("Warning - a is very large – results may be inaccurate")
</pre>
<pre>
# example 2 – if and else check to tell user if a value is in an expected range

if a > 1000 or a < 0:
    print("Warning - a is outside expected range of 0-1000")
else:
    print("Information - a is in normal range")
</pre>
<pre>
# example 3 – code to check a variable a is 0 to 5, correct it to this range if not, and report on what it is doing 

if a > 5:
    print("a was too big, setting to 5")
    a = 5
elif a < 0:
    print("a was too small, setting to 0")
    a = 0
else:
    print("a was in correct range 0-5")
</pre>
