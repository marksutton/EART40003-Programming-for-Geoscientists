---
---
{% raw %}
# demo_6_test1.py

Return to [Demonstration programs](index.md).

````python
# test1.py - reads in a csv, appends a number to each line,
#            and writes it out again to a new csv file

testfile = open("test.csv", "r")    # open file for reading
datalines = testfile.readlines()    # read all lines into list
testfile.close()                    # close the file

# comprehension to strip newlines, and add ",20" to each line
# also has to add a newline again before I can write it back
datalines = [line.strip()+",20\n" for line in datalines]

testfile = open("test-m.csv", "w")  # open output file for writing
testfile.writelines(datalines)      # write all lines from list
testfile.close()                    # ... and close it
````
{% endraw %}
