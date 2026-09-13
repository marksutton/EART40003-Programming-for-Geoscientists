try / except (exception handling)
============

Exceptions are run-time errors like divide by zero, failed conversions from string to text, etc. You don’t want these appearing when a program runs if you can avoid it. You can either write code that checks for problems before it does the step that throws the error (e.g. check that a string only includes digits before trying to convert it), or you can let the exception occur and catch it – write code that intercepts it and does something more elegant than crashing. The syntax is:

<pre>
try:
    [lines to execute]
except ExceptionName1:
    [lines to execute if ExceptionName1 happened]
except ExceptionName2:
    [lines to execute if ExceptionName2 happened]
…
except:
    [lines to execute if there was an exception not caught above]
else:
    [lines to execute if there was no exception at all]
</pre>

‘else’ is optional, and multiple except blocks are also optional – but if you have a ‘try’ you have to have at least one ‘except’.

For instance, the following code will continue to loop until the user enters a valid number that does not cause the float function to throw an exception

<pre>
while True: 
    response = input("Enter a number ")
    try:
        numeric_response = float(response)
        break
    except:
        print("You did not enter a number, please try again.")
</pre>

Exception names are not going to be guessable – they are things like `DivideZeroError`, and you need to get them exactly right. They can be looked up, but it’s almost always simpler to simply do something that generates the error, then see what it is! For instance…

<pre>a = "ten"
a = float(a)
</pre>

Will generate an exception, as the float function won’t like the string "ten". If you run this, you get…

<pre>
Traceback (most recent call last):
  File "d:/Teaching/Programming/test.py", line 2, in <module>
    a = float(a)
ValueError: could not convert string to float: 'ten'
</pre>
… which tells you (on the last line) that this error is called ValueError.


