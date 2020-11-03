Methods for str (built-in string class)
======================

These are methods not functions, so the syntax uses the ‘.’ after an object of type str. For example, use `"hello".capitalize()` not `capitalize("hello")`. There are many string methods – not all are listed here, and for some that are there are optional extra arguments that I do not document here.

**capitalize() return type: str**
<br />Returns a version of the string with the initial letter capitalized. 

**count(substring) return type: int**
<br />Counts how many times ‘substring’ occurs in the string, then returns this count (which may be 0) as an integer.

**find(substring) return type: int**
<br />Returns the index (position) of the first occurrence of ‘substring’ occurs in the string. If substring isn’t found, it returns -1.

**isalpha() return type: bool**
<br />Returns True if all characters in the string are letters, otherwise returns False

**isnumeric() return type: bool**
<br />Returns True if all characters in the string are digits, otherwise returns False

**join(container) return type: string**
The opposite of *split*. Join takes a container (e.g. a list, normally a list of strings) as an argument and joins all the elements together into a single string, using the object string as a separator. For example, `",".join(["goodbye", "cruel", "world"])` returns the string "goodbye,cruel,world".

**lower() return type: str**
<br />Returns a copy of the string with all characters converted to lowercase.

**replace(oldtext, newtext) return type: str**
<br />Returns a copy of the string in which all occurrences of the text oldtext are replaced with newtext. 

**split(split_on) return type: list (of strings)**
Splits a string on the substring split_on into a list of strings. For example, `"goodbye cruel world".split(" ")` returns `["goodbye", "cruel", "world"]`. split_on is normally one a one-character string, but it doesn't have to be. 

**strip() return type: str**
<br />Returns a copy of the string with any whitespace characters (spaces, tabs, newlines) removed from both the start and end

**upper() return type: str**
<br />Returns a copy of the string with all characters converted to uppercase.

