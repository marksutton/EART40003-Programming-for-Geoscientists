Variables
=========

Variables are values that have been assigned a name. A better way to think of them might be as boxes in the computers memory that can store something (a number, a string etc.), 
and that have a name for us to refer to them by. 


Variable names
--------------
Variable names in Python can be any length and can consist of uppercase and lowercase letters (A-Z, a-z), digits (0-9), and the underscore character (_).
Most important, note that they cannot include spaces! An additional restriction is that, although a variable name can contain digits, 
the first character of a variable name cannot be a digit. There are also a few names you can’t use, as they have special meanings. 
These are: *False, def, if, raise, none, del, import, return, True, elif, in, try, and, else, is, while, as, except, lambda, with, assert, finally, 
nonlocal, yield, break, for, not, class, from, or, continue, global, pass.*  

Variable names are case sensitive – so `MyVariable` is NOT the same variable as `Myvariable`. This is a common source of errors, so look out for it.  

Variable names should be meaningful – they should help someone reading your code understand what the variable is used for. 
Avoid single-letter variables (I’ve used some in some examples to save space, or where the example doesn't make clear what the value really represents, but you shouldn't). 
Don’t worry about how long it takes to type longer names – Spyder has an auto-fill feature that will bring them up for you if you start typing – 
but a good maximum length though would be ~20 characters. 
Where variable names incorporate multiple words (recall that you can’t use spaces), 
avoid just running them together (so `accelerationduetogravity` is bad – it’s hard to read). In these cases you can use either:
* `accelerationDueToGravity` (this is called Camel Case)
* `AccelerationDueToGravity` (this is called Pascal Case)
* `acceleration_due_to_gravity` (using underscores for spaces - this is called snake case)  

It really doesn’t matter which of these you use, but try to be consistent.
