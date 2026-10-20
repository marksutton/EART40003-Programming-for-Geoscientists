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

{% raw %}
```python
print(f"Found {other_variable} open braces {{")
```
{% endraw %}

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

## String slicing syntax

Python provides a flexible and easy-to-use way to extract bits of strings (compared to many other languages, which often make heavy-going of this). This involves appending the string with [x:y], where x is the first character you want, and y is the first character that you don’t want – so if you want characters 3-7, x will be 3, y will be 8. If you only want one character at position x, you can write [x]. There are a few shortcuts and conventions to this, which are best explained by example (so see examples below). Counting starts at 0 (so “hello”[1] is “e” not “h”). You can put the [] after a string value in quotes, or a string variable, or even a string expression – so **(string1 + string2)[10:20]** is legal Python – meaning join string2 to string1, then give me the string between character 10 and 20 of the combined string. Note the brackets – this makes sure that the joining is done before the slicing (just like brackets in numerical expressions). Some examples of string-slicing:

| Expression | Meaning – Value | Expression | Meaning - Value |
| --- | --- | --- | --- |
| `"slicing"[0]` | Character 0 - `"s"` | `"slicing"[4:]` | Character 4 to end – `"ing"` |
| `"slicing"[1:3]` | Characters 1-2 – `"li"` | `"slicing"[-4:-2]` | Characters 4<sup>th</sup> from end to 3<sup>rd</sup> from end – `"ci"` |
| `"slicing"[:5]` | Start to character 4 – `"slici"` | `"slicing"[-4:]` | Characters 4<sup>th</sup> from end to end (i.e. last 4 characters) – `"cing"` |

## String methods

These are methods not functions, so the syntax uses the ‘.’ after an object of type str. For example, use **"hello".capitalize()** not **capitalize("hello")**. There are many string methods – not all are listed here, and for some that are there are optional extra arguments that I do not document here.

### `capitalize()`

**Returns:** str

Returns a version of the string with the initial letter capitalized.

### `count(substring)`

**Returns:** int

Counts how many times ‘substring’ occurs in the string, then returns this count (which may be 0) as an integer.

### `find(substring)`

**Returns:** int

Returns the index (position) of the first occurrence of ‘substring’ occurs in the string. If substring isn’t found, it returns -1.

### `isalpha()`

**Returns:** bool

Returns True if all characters in the string are letters, otherwise returns False

### `isnumeric()`

**Returns:** bool

Returns True if all characters in the string are digits, otherwise returns False

### `lower()`

**Returns:** str

Returns a copy of the string with all characters converted to lowercase.

### `replace(oldtext, newtext)`

**Returns:** str

Returns a copy of the string in which all occurrences of the text *oldtext* are replaced with *newtext*.

### `strip()`

**Returns:** str

Returns a copy of the string with any whitespace characters (spaces, tabs, newlines) removed from both the start and end

### `upper()`

**Returns:** str

Returns a copy of the string with all characters converted to uppercase.

### `split(split_on)`

**Returns:** list (of strings)

Splits a string on the substring *split_on* into a list of strings. For example, **"goodbye cruel world".split(" ")** returns **["goodbye", "cruel", "world"]**. *split_on* is normally one a one-character string, but it doesn't have to be.

### `join(container)`

**Returns:** string

The opposite of *split*. Join takes a container (e.g. a list, normally a list of strings) as an argument and joins all the elements together into a single string, using the object string as a separator. For example, **",".join(["goodbye", "cruel", "world"])** returns the string **"goodbye,cruel,world".**

Use **",".join(mylist)** not **join(mylist,",")**.

[Return to the site index](index.md)
