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
You can add strings to join them together with the \+ operator. To mix numbers and text together into a string, use 'f strings' (see below).

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

String slicing syntax
--------

Python provides a flexible and easy-to-use way to extract bits of strings (compared to many other languages, which often make heavy-going of this). This involves appending the string with `[x:y]`, where x is the first character you want, and y is the first character that you don’t want – so if you want characters 3-7, x will be 3, y will be 8. If you only want one character at position x, you can write `[x]`. There are a few shortcuts and conventions to this, which are best explained by example (so see examples below). Counting starts at 0 (so `"hello"[1]` is “e” not “h”). You can put the [] after a string value in quotes, or a string variable, or even a string expression – so `(string1 + string2)[10:20]` is legal Python – meaning join string2 to string1, then give me the string between character 10 and 20 of the combined string. Note the brackets – this makes sure that the joining is done before the slicing (just like brackets in numerical expressions). Some examples of string-slicing:

`"slicing"[0]`: means character 0 - so "s"
<br />`"slicing"[1:3]`: means characters 1-2 – so “li”
<br />`"slicing"[:5]`:	Start to character 4 – so “slici”. Yes, it DOES mean character 4 - it's up to but not including character 5.
<br />`"slicing"[4:]`: means character 4 to end – so “ing”
<br />`"slicing"[-4:-2]`:	means characters 4th from end to 3rd from end – so “ci”. Yes it DOES mean 3rd from the end - it's up to but not including character -2 from the end.
<br />`"slicing"[-3:]`	Characters 3rd from end to the end (i.e. last 3 characters) – so “ing”

f Strings
--------

'f strings' (properly called 'formatted string literals') provide a way to insert values (normally from variables) into a string. This is a very common thing to want to do! Before going into the details of how they work, I should point out that there are at least three other ways to do this, and if you look at code available online you may see these other approaches being used. The 'f string' approach though is the most modern and probably the most convenient, so you should use it in this course.
<br />
<br />
In their simplest form, you use f strings by just inserting variable names into strings inside braces { }, and prefixing the " at the start of the string with an f. There are some complexities though - these are best explained by examples.
<br />
*In these examples, `my_variable` has the floating point value 4.21, `my_string` is `"hello"`, and `other_variable` has the integer value 8. In each case I give the output or effect in a comment*
<pre>
print(f"Result is {my_variable}")                          # prints "Result is 4.29"
print(f"{my_string}, the result is {my_variable}")          # prints "hello, the result is 4.29" (you can have multiple variables in braces, and can include strings)
print(f"Result is {my_variable + 2.1}")                     # prints "hello, the result is 6.49"  (you can do calculations inside the braces!)
print(f"Found {other_variable} open braces {{")             # prints "Found 8 open braces {"  (to use a { or } in an f string you have to double it)
new_string = f"Value is {my_variable}"                      # sets new_string to "Value is 4.29" (you can use f strings outside of print functions!)
print(f"Result to one d.p. is {my_variable:.1f}")           # prints "Result to one d.p. is 4.3" (the :.1f specifies number of decimal places - very useful!)
print(f"Result to four d.ps is {my_variable:.4f}")          # prints "Result to one d.ps is 4.2900" (and again)
print(f"Result is {other_variable:02}")                     # prints "Result is 08" (02 means use two columns, padding with leading zeros)
print(f"Result is {other_variable:2}")                      # prints "Result is  8" (2 means use two columns, padding with spaces)
print(f"Result is {my_variable:07.3f}")                     # prints "Result is 004.290" (you can combine padding with decimal places - but padding counts total characters)
</pre>

There *is* more to the complex world of string formatting, but the examples above should cover most of what you want to do. See e.g. https://zetcode.com/python/fstring/ for more details if you need them.






</pre>
