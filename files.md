File handling
================

File handling in Python is pretty straightforward, though it can involve quite a few steps. 
First you open the file using the built-in open function, specifying whether you are opening for reading, writing or appending. 
This returns a 'file' object. You then read or write lines of text to the file using various methods of the file object (see above). 
Finally, you finish by closing the file, using the close method of the file object.  

Opening a file:
--------------

<pre>data_file = open("myfile.csv", "r")    # open file for reading
</pre>

`myfile.csv` is the filename, and the second string specifies the mode – it will be either "r" for read, "w" for write, or "a" for append. 
"a" and "w" modes are both used for outputting data to files – but in "w" mode any existing data in the file is overwritten, and in "a" mode it's preserved – 
new data goes at the end. With either "a" or "w" the file is created if it doesn't already exist.

Two things to watch for with filenames. 
First, you DO need the extension (the .csv). Be aware that Windows, by default, 
hides file extensions so you can't see them - it really shouldn't, but it does. So if you look in Windows Explorer, 
you'll probably see that the file is just called 'myfile'. The extension (.csv in this case) IS there though, and you need it to read it in Python. 
Consider turning off the Windows extension-hiding feature. It's one of the first things I do whenever I get a new machine. 
Second – you may need a 'path' to the file. Python will look in the working folder that you specified when you set up VSCode, 
and if the file isn't there, it won't be able to open it. If it's in a folder 
underneath that (for instance my files for this session are in 'Session6' under my root programming folder), just use the name of that folder, thus:

<pre>data_file = open("Session6/myfile.csv", "w")
</pre>

Alternatively you can use an 'absolute' path – something like

<pre>data_file = open("C:/programming/Session6/myfile.csv", "w")
</pre>

If Python can't open the file, open will throw an exception. Possible reasons for failure are:
* You tried to open a file to read that doesn't exist (or at least doesn’t exist where you said it should be)
* You tried to open a file for writing with an illegal filename
* You tried to open a file for writing and it was 'locked' because some other program was using it

Once the file is opened, everything else you do with it uses methods of the file object (i.e. the thing that open returned – data_file in the example above).

Another very annoying complication with paths occurs on Windows system. Almost all computer system use the / character in paths to indicate folders within folders. Windows, for reasons lost in the mists of time, uses a backslash instead (\). The problem with this is that all programming languages use \ in strings to indicate ‘special character’ – we’ve already seen \n meaning newline. So if you try entering a normal windows path using \ into a python string (i.e using what you get if you copy/paste the path out of a windows explorer window) and opening a file – it won’t work, so 

<pre>data_file = open("C:\programming\Session6\myfile.csv", "w")
</pre>

will fail – Python thinks `\p` ,`\S` and `\m` are special characters, and gets confused.

To get round this, you can either use forward slashes (python is clever enough to know it’s on a Windows system and turn them into backslashes behind the scenes to make the system open the file), OR use double backslashes, which is the standard way to put an actual backslash character into a string (this is the same principle as using %% for a % symbol, as a single % is used to start a placeholder). So

<pre>data_file = open("C:\\programming\\Session6\\myfile.csv", "w")
</pre>

Will work!


Reading from a file
-------------------

There are several read methods you can use, depending on exactly what you need to do.

<pre>string_data = data_file.read()   # read it all into a string
</pre>

Reads the entire file into a string. Sometimes this is what you want (for small files), but more commonly you want to read data in smaller chunks. You can do…

<pre>string_data = data_file.read(5)  # read 5 characters
</pre>
… to read a set number of characters. If you call it again, you'll get the next 5 characters. 
For some file formats this might be useful – sometimes data IS in chunks of a standard size - but a more common requirement is to read in files a line at a time.

<pre>a_line = data_file.readline()  # read in the next line
</pre>

This does what you expect – it reads in an entire line, and puts it into the string variable a_line. The next time you call it, it will read the next line - if there are no more lines, it returns an empty string. Obviously if you use this, you are likely to be using it within a loop to read all the lines. Don't forget to check for empty strings (length 0) to see if you've reached the end. One quirk to be aware of – the string will include the invisible 'newline' character at the end, so if your line was just "1,2,3" then the read string would be length 6 not length 5, and if you printed it you would find an unexpected line-break appearing. This does mean though that you can tell a blank line (which will be length 1, because of the line-break) from the end-of-file (length 0).

Finally, and probably most usefully of all, you can read the entire file in with one go into a list of strings, one for each line. 

<pre>all_data_from_file = data_file.readlines()  # read it all into list
</pre>

So `all_data_from_file[0]` will be give a string with the first line of the file, `all_data_from_file[-1]` will give the last line, etc.

Like readline, readlines leaves the new-line character in the strings. Whether or not this matters depends on what you are going to do with the data, 
but you will often want to remove these newlines. One way to remove this is the `strip` method of the string class, which is designed to remove ‘whitespace’ 
characters (spaces, newlines etc.) from the ends of strings. So, with a list comprehension, you could do:

<pre>all_data_from_file = [line.strip() for line in data_file.readlines()]  
</pre>

Writing to a file
-----------------

To simply output a string to a file, use the write method (you obviously need to open the file first in write mode - see above).

<pre>data_file.write("some text”)
</pre>

or to write a list of strings, you can use the writelines method

<pre>data_file.writelines(list_of_strings)
</pre>

Note that neither `write` nor `writeline`s puts a new-line character at the end of the strings, so you have to do that yourself if you want each on a new line. 
Easy enough with write, just add "\n" to the string, but with `writelines` it’s a minor pain as you need to go through the list 
and add in the "\n" to each element. A list comprehension to do this is:

<pre>data_file.writelines(s+"\n" for s in list_of_strings)
</pre>

or you can do it with join and write – turn the list into one string with new-lines as a separator, and write it.

<pre>data_file.write("\n".join(list_of_strings))
</pre>

Closing a file
--------------

This is easy! Whatever mode you opened the file in, just use the close() method of the file object. e.g. 

<pre>data_file.close()
</pre>

Once you've closed a file you can no longer read or write to it (though you could of course open it again later if you really wanted to). You don't actually HAVE to close files (i.e. Python won't complain), but if you leave them open, other programs can't use them. They should automatically close when your program finishes, but its nonetheless good practice to close them as soon as you've finished using them. 
