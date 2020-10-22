Loops – code blocks executed repeatedly – are fundamental to most non-trivial programs.  
Python has two types of loops – while loops, and for loops. 

for loops
--------
Not covered yet!

while loops
---------
while loops are very simple in concept, and are general-purpose loops. They begin with a `while` statement that contains a condition. This is followed 
by one of more lines of code to be executed repeatedly, as long as the condition of the while statement continues to be true.
This code has to be indented to tell python which lines are within the while block.

<pre>
while condition:
    Code to execute as long as condition is True (can be as many lines as needed)
</pre>

e.g. this loop uses a counter variable to go round 5 times, printing out the numbers 1 to 5 

<pre>
counter = 0
while counter < 5:
    counter = counter + 1
    print(counter)
</pre>

Note that the condition is evaluated BEFORE each iteration of the loop, and if it’s False the first time round, the code inside the loop will not run even once. So…  

<pre>
counter = 5
while counter < 5:
    counter = counter + 1
    print(counter)
</pre>

… will print nothing – the condition is False the first time it’s encountered, so the indented code never gets executed.

Your condition doesn’t have to use a counter – it can be any legal condition (see below for more on conditions). You could for instance put an input statement inside a loop, and keep going round until the user types in a number that is within a certain range.  

See break and continue below for some ways to do more subtle loop control within a loop.  

Common errors to watch out for with while loops:
*	Infinite loops. If for instance you use a counter variable and forget to increase it each time, your loop will never finish – the condition will always be false. You can stop an accidental infinite loop using Ctrl-C (in the terminal window), though this stops the entire program. Just occasionally you WANT an infinite loop, so it’s not illegal to make one.
* Forgetting indentation, or inconsistent number of spaces in indentation. You HAVE to indent the statements that you want to happen inside the loop (to the same level).

break and continue
-----------------

These two keywords are used as statements. They work in both for and while loops.  
**break** ends the loop – execution of the program moves to the line immediately after the loop.  
**continue** ends this iteration of the loop – execution of the program moves back to the `while` to test the condition (or to the `for` if this is a for loop).  

e.g. this version of the counter program uses continue to skip iteration 3 – it will print 1,2,4,5
<pre>
counter = 0
while counter < 5:
    counter = counter + 1
    if counter == 3:
        continue
    print(counter)
</pre>
  
e.g. this version of the program uses break to stop the loop early if the user requested it via input  
<pre>
stop = input("Stop at 10? (y/n) ")

counter = 0
while counter < 100:
    counter = counter + 1
    if counter > 10 and stop == "y":
        break
    print(counter)
</pre>
