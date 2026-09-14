# Strings

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

[Return to the site index](index.md)
