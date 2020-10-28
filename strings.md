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

String slicing syntax
--------

Python provides a flexible and easy-to-use way to extract bits of strings (compared to many other languages, which often make heavy-going of this). This involves appending the string with `[x:y]`, where x is the first character you want, and y is the first character that you don’t want – so if you want characters 3-7, x will be 3, y will be 8. If you only want one character at position x, you can write `[x]`. There are a few shortcuts and conventions to this, which are best explained by example (so see examples below). Counting starts at 0 (so `"hello"[1]` is “e” not “h”). You can put the [] after a string value in quotes, or a string variable, or even a string expression – so `(string1 + string2)[10:20]` is legal Python – meaning join string2 to string1, then give me the string between character 10 and 20 of the combined string. Note the brackets – this makes sure that the joining is done before the slicing (just like brackets in numerical expressions). Some examples of string-slicing:

`"slicing"[0]`: means character 0 - so "s"
<br />`"slicing"[1:3]`: means characters 1-2 – so “li”
<br />`"slicing"[:5]`:	Start to character 4 – so “slici”. Yes, it DOES mean character 4 - it's up to but not including character 5.
<br />`"slicing"[4:]`: means character 4 to end – so “ing”
<br />`"slicing"[-4:-2]`:	means characters 4th from end to 3rd from end – so “ci”. Yes it DOES mean 3rd from the end - it's up to but not including character -2 from the end.
<br />`"slicing"[-3:]`	Characters 3rd from end to the end (i.e. last 3 characters) – so “ing”

