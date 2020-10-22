Strings
=============

In programming, text is called a 'string' (because it is a string of characters). Strings occur all the time in code - sometimes they just represent text you want to appear on screen,
but sometimes you do genuine processing and coding on strings as well.  
Strings can be stored in variables, just like numbers can.  
To indicate that stuff you type should be treated as a string, surround it with either single or double-quotes (' or " - the latter is the shift-2 character, not two single quotes 
next to each other). If you don’t do this, python will try to treat the text as a variable name or a statement, and things will go wrong.

<pre>
print("Hello")  # prints Hello
print(Hello)    # Error
</pre>
In the second example python will treat `Hello` as a variable name and try to find it's value and print it. If you don't have a variable called Hello, you will get an error.

Manipulating strings
-----------------
You can add strings to join them together with the \+ operator. To mix numbers and text together into a string, use the % operator. See [operators](operators.md) for more details

Line breaks
--------
To include a new-line in a string (the equivalent of hitting return - a line break) you have two options – 
you can use `\n` (which prints as a line-break) or you can surround your string with triple double quotes, then use actual line breaks. So both of the following examples:
<pre>print("new\nline")
</pre>
<pre>print("""new
line""")</pre>

will print as
<pre>new  
line</pre>


