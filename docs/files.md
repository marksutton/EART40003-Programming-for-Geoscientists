# File handling

File handling in Python is pretty straightforward, though it can involve quite a few steps. First you open the file using the built-in [*open* function](functions.md#openfilename-mode), specifying whether you are opening for reading, writing or appending. This returns a 'file' object. You then read or write lines of text to the file using various methods of the file object (see [File methods](#file-methods)). Finally, you finish by closing the file, using the close method of the file object.

## Opening a file

```python
data_file = open("myfile.csv", "r")    # open file for reading
```

myfile.csv is the filename, and the second string specifies the mode – it will be either "r" for read, "w" for write, or "a" for append. "a" and "w" modes are both used for outputting data to files – but in "w" mode any existing data in the file is overwritten, and in "a" mode it's preserved – new data goes at the end. With either "a" or "w" the file is created if it doesn't already exist.

Two things to watch for with filenames. First, you DO need the extension (the .csv). Be aware that Windows, by default, hides file extensions so you can't see them - it really shouldn't, but it does. So if you look in Windows Explorer, you'll probably see that the file is just called 'myfile'. The extension (.csv in this case) IS there though, and you need it to read it in Python. Consider turning off the Windows extension-hiding feature. It's one of the first things I do whenever I get a new machine. Second – you may need a 'path' to the file. Python will look in the folder that your .py file is in, and if the file isn't there, it won't be able to open it. If it's in a folder underneath that (for instance my files for this session are in 'Session6' under my root programming folder), just use the name of that folder, thus:

```python
data_file = open("Session6/myfile.csv", "w")
```

Alternatively you can use an 'absolute' path – something like

```python
data_file = open("C:/programming/Session6/myfile.csv", "w")
```

If Python can't open the file, *open* will throw an exception. Possible reasons for failure are:

- You tried to open a file to read that doesn't exist (or at least doesn’t exist where you said it should be)

- You tried to open a file for writing with an illegal filename

- You tried to open a file for writing and it was 'locked' because some other program was using it.

Once the file is opened, everything else you do with it uses methods of the file object (i.e. the thing that *open* returned – **data_file** in the example above).

Another very annoying complication with paths occurs on Windows systems. Almost all computer systems use the / character in paths to indicate folders within folders. Windows, for reasons lost in the mists of time, normally uses a backslash instead (\). The problem is that backslashes have special meanings inside Python strings - for example, we've already seen \n meaning newline. As a result, a Windows path copied directly into a Python string may not mean what you expect, and in some cases will produce an error.

```python
data_file = open("C:\programming\Session6\myfile.csv", "w")
```

This will fail – Python thinks \p, \S and \m have special meanings, and gets confused.

To get round this, you can either use forward slashes (python is clever enough to know it’s on a Windows system and turn them into backslashes behind the scenes to make the system open the file), OR use double backslashes, which is the standard way to put an actual backslash character into a string. So

```python
data_file = open("C:\\programming\\Session6\\myfile.csv", "w")
```

Will work!

## Reading from a file

There are several read methods you can use, depending on exactly what you need to do.

```python
string_data = data_file.read()   # read it all into a string
```

Reads the entire file into a string. Sometimes this is what you want (for small files), but more commonly you want to read data in smaller chunks. You can do…

```python
string_data = data_file.read(5)  # read 5 characters
```

… to read a set number of characters. If you call it again, you'll get the next 5 characters. For some file formats this might be useful – sometimes data IS in chunks of a standard size - but a more common requirement is to read in files a line at a time.

```python
a_line = data_file.readline()  # read in the next line
```

This does what you expect – it reads in an entire line, and puts it into the string variable *a_line*. The next time you call it, it will read the next line - if there are no more lines, it returns an empty string. Obviously if you use this, you are likely to be using it within a loop to read all the lines. Don't forget to check for empty strings (length 0) to see if you've reached the end. One quirk to be aware of – the string will include the invisible 'newline' character at the end, so if your line was just "1,2,3" then the read string would be length 6 not length 5, and if you printed it you would find an unexpected line-break appearing. This does mean though that you can tell a blank line (which will be length 1, because of the line-break) from the end-of-file (length 0).

Finally, and probably most usefully of all, you can read the entire file in with one go into a list of strings, one for each line.

```python
all_data_from_file = data_file.readlines()  # read it all into list
```

So **all_data_from_file[0]** will be given a string with the first line of the file, **all_data_from_file[-1]** will give the last line, etc.

Like *readline*, *readlines* leaves the new-line character in the strings. Whether or not this matters depends on what you are going to do with the data, but you will often want to remove these newlines. One way to remove this is the *strip* method of the string class, which is designed to remove ‘whitespace’ characters (spaces, newlines etc.) from the ends of strings. So, with a list comprehension, you could do:

```python
all_data_from_file = [line.strip() for line in data_file.readlines()]
```

## Writing to a file

To simply output a string to a file, use the *write* method:

```python
data_file.write("some text")
```

or to write a list of strings, you can use the *writelines* method

```python
data_file.writelines(list_of_strings)
```

Note that neither write nor writelines puts a new-line character at the end of the strings, so you have to do that yourself if you want each on a new line. Easy enough with *write*, just add **"\n"** to the string, but with writelines it’s a minor pain as you need to go through the list and add in the **"\n"** to each element. A list comprehension to do this is:

```python
data_file.writelines([s+"\n" for s in list_of_strings])
```

or you can do it with *join* and *write* – turn the list into one string with new-lines as a separator, and write it.

```python
data_file.write("\n".join(list_of_strings))
```

## Closing a file

This is easy! Whatever mode you opened the file in, just use the close() method of the file object. e.g.

```python
data_file.close()
```

Once you've closed a file you can no longer read or write to it (though you could of course open it again later if you really wanted to). You don't actually HAVE to close files (i.e. Python won't complain), but if you leave them open, other programs often can't use open files. They should automatically close when your program finishes, but it's nonetheless good practice to close them as soon as you've finished using them.

> **Technical note — optional:** Python also provides a `with open(...)` syntax which automatically closes the file when you have finished with it. This is commonly preferred in larger programs, but explicit `open()` and `close()` are used here to make the individual file-handling steps clear.

## File methods

These are methods not functions, so the syntax uses the ‘.’ after an object of type *file*. For example, use **myfile.close()** not **close(myfile)** to close the file. You get a *file* object by using the [open function](functions.md#openfilename-mode).

### `close()`

**Returns:** N/A

Closes the file – use when you’ve finished with it. If you don’t close files, other programs often can't use open files until your program exits. Get into the habit of closing them as soon as you’ve finished with them.

### `read(characters)`

**Returns:** string

Returns up to *characters* characters from the file as a string. If you omit *characters*, you get the entire file.

### `readline()`

**Returns:** string

Reads the next line from the file into a string. *readline* does NOT strip the new-line character from the end of the line – it will be there in your string - remove it with the string *strip* method if you don’t want it, which you normally won’t. If there are no more lines available, *readline* returns an empty string (length 0).

### `readlines()`

**Returns:** list of strings

Reads the file into a *list* – each line becomes a string element. This is the most common way to read in scientific data in tables (e.g. in a csv file). Each line retains the newline character at the end, as with *readline*.

### `write(string)`

**Returns:** int

Writes the string argument to the file and returns the number of characters written. Does NOT append a new-line character automatically.

### `writelines(stringlist)`

**Returns:** N/A

Writes all elements in *stringlist* to the file. *stringlist* must, unsurprisingly, be a list of strings. Does NOT append a new-line character after each string – see [Writing to a file](#writing-to-a-file) for ways to get round this.

[Return to the site index](index.md)
