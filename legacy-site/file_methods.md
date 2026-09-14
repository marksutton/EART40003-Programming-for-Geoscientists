file (built-in file-handling class)
===================================

These are methods not functions, so the syntax uses the ‘.’ after an object of type file. For example, use `myfile.close()` not `close(myfile)` 
to close the file. You get a file object by using the open function – see [functions](functions.md) document.

**close() return type: N/A**
<br />Closes the file – use when you’ve finished with it. If you don’t close files, no other program can use them until your program exits. Get into the habit of closing them as soon as you’ve finished with them. 

**read(character_count) return type: string**
<br />Returns up to `character_count` characters from the file as a string. If you omit `character_count`, you get the entire file.

**readline() return type: string**
<br />Reads the next line from the file into a string. `readlines` does NOT strip the new-line character from the end of the line – 
it will be there in your string - remove it with the string `strip` method if you don’t want it, which you normally won’t. 
If there are no more lines available, `readlines` returns an empty string (length 0).

**readlines() return type: list of strings**
<br />Reads the file into a list – each line becomes a string element. This is the most common way to read in scientific data in tables (e.g. in a csv file). 
Each line retains the newline character at the end, as with `readline`.

**write(string) return type: N/A**
<br />Writes the string argument to the file. Does NOT append a new-line character automatically.

**writelines(stringlist) return type: N/A**
<br />Writes all elements in `stringlist` to the file. `stringlist` must, unsurprisingly, be a list of strings. 
Does NOT append a new-line character after each string – see [files](files.md) document for ways to get round this. 
