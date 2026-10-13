# try / except

Exceptions are run-time errors like divide by zero, failed conversions from strings to numbers, etc. You don’t want these appearing when a program runs if you can avoid it. You can either write code that checks for problems before it does the step that throws the error (e.g. check that a string only includes digits before trying to convert it), or you can let the exception occur and *catch* it – write code that intercepts it and does something more elegant than crashing. The syntax is:

<div class="syntax-template" style="font-family:inherit; background:#f4f7fa; border-left:3px solid #5483bc; padding:0.5em 0.8em; margin:0.8em 0">
<p style="margin:0">try:</p>
<p style="margin:0">    [lines to execute]</p>
<p style="margin:0">except ExceptionName1:</p>
<p style="margin:0">    [lines to execute if ExceptionName1 happened]</p>
<p style="margin:0">except ExceptionName2:</p>
<p style="margin:0">    [lines to execute if ExceptionName2 happened]</p>
<p style="margin:0">…</p>
<p style="margin:0">except Exception:</p>
<p style="margin:0">    [lines to execute if there was an exception not caught above]</p>
<p style="margin:0">else:</p>
<p style="margin:0">    [lines to execute if there was no exception at all]</p>
</div>


‘else’ is optional, and multiple except blocks are also optional – but if you have a ‘try’ you have to have at least one ‘except’.

> **Best practice:** When catching exceptions, mention specific exceptions whenever possible instead of using a ‘bare except’ (i.e just `except:`). A bare except will catch `SystemExit` and `KeyboardInterrupt` exceptions, making it harder to interrupt a program with Control-C, and can disguise other problems. If you want to catch all exceptions that signal program errors, use `except Exception:`

Exception names are not going to be guessable – they are things like ZeroDivisionError, and you need to get them exactly right. They can be looked up, but it’s almost always simpler to simply do something that generates the error, then see what it is! For instance…

```python
a = "ten"
a = float(a)
```

Will generate an exception, as the float function won’t like the string **"ten".** If you run this, you get…

```text
Traceback (most recent call last):
  File "d:/Teaching/Programming/test.py", line 2, in <module>
    a = float(a)
ValueError: could not convert string to float: 'ten'
```

… which tells you that this exception is called ValueError.

[Return to the site index](index.md)
