Loops – code blocks executed repeatedly – are fundamental to most non-trivial programs.  
Python has two types of loops – while loops, and for loops. 

for loops
--------

One of the more refreshingly simple things about Python is that it only has two types of loops (some languages have a whole profusion of them). We have already seen while loops - for loops are the other Python loop-type. for loops are used for iterating (looping) over 'iterables' – which are containers with multiple values, like lists. As such they are a little more specialised than the general-purpose while loops, but are nonetheless even more commonly used. Their syntax is:

<pre>
for item in iterable:
    [one or more lines to execute each time round loop]
</pre>

This will loop round as many times as there are elements in the iterable container object (which is often going to be a list). The first time round the loop, the variable item will have the value of the first element. The second time, it will have the value of the second element… etc. For example…

<pre>
my_list = [1,10,100]
for number in my_list:
    print(number)
</pre>

… will print 1, 10 and 100. While technically what a for loop does is iterate over an iterable, in practice you can also use it to just loop a certain number of times. In earlier sessions, you will recall that we have built counter loops using 'while' to do that  – we set a counter to 0, our while condition checked the counter to see if it had reached a desired maximum, and each time round the loop we added 1 to it. This worked fine and was good practice (NOT a waste of time!), but for loops in conjunction with the range function provide a more efficient way to do this.

The range function (see [functions](functions.md)) is used to make sequences of integers, and returns something that's 'almost but not quite a list'. See above for details. This slightly odd 'list-like thing' that it returns is an iterable, i.e. you can use for loops on it – in fact getting used in for loops is the most important purpose of the range function. So…

<pre>
for number in range(10):   # loop 10 times, number will take values 0, 1… 9
    [do stuff]
</pre>

Does the same as the code below, but is much more concise.

<pre>
number = 0
while number<10:
    [do stuff]
    number += 1
</pre>

Common errors with for loops
* Forgetting the : at the end
* Using the range stop value incorrectly – remember that range(0, 10) generates 0-9, not 0-10.
* Forgetting to indent. This is not optional!
* Getting confused with while. If you put a condition in a for loop it doesn't work! It needs an item name, and a container/iterable name.  


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
*	Infinite loops. If for instance you use a counter variable and forget to increase it each time, your loop will never finish – the condition will always be false. You can stop an accidental infinite loop using Ctrl-C (in the console window), though this stops the entire program. Just occasionally you WANT an infinite loop, so it’s not illegal to make one.
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
