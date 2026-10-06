# While loops

Loops - code blocks executed repeatedly - are fundamental to most non-trivial programs. Python has two types of loops - `while` loops, and `for` loops (we will cover `for` loops later). `while` loops are very simple in concept, and are general-purpose loops. They begin with a `while` statement that contains a condition, which is followed by one or more lines of code to be executed repeatedly, as long as the condition continues to be true. This code has to be indented to tell Python which lines are within the while block.

<div class="syntax-template" style="font-family:inherit; background:#f4f7fa; border-left:3px solid #5483bc; padding:0.5em 0.8em; margin:0.8em 0">
<p style="margin:0"><strong>while <em>condition</em>:</strong></p>
<p style="margin:0">    Code to execute as long as condition is True (can be as many
lines as needed)</p>
</div>


E.g. this loop uses a counter variable to go round 5 times, printing out the numbers 1 to 5:

```python
counter = 0
while counter < 5:
    counter = counter + 1
    print(counter)
```

Note that the condition is evaluated BEFORE each iteration of the loop, and if it's False the first time round, the code inside the loop will not run even once. So...

```python
counter = 5
while counter < 5:
    counter = counter + 1
    print(counter)
```

...will print nothing - the condition is False the first time it's encountered, so the indented code never gets executed.

Your condition doesn't have to use a counter - it can be any legal condition (see [Conditions](conditions.md) for more on conditions). You could for instance put an input statement inside a loop, and keep going round until the user types in a number that is within a certain range.

See [*Break and continue*](#break-and-continue) below for some ways to do more subtle loop control within a `while` loop.

## Common errors

- Infinite loops. If for instance you use a counter variable and forget to increase it each time, your loop will never finish - the condition will always be true. You can stop an accidental infinite loop using Ctrl-C (in the console window), though this stops the entire program. Just occasionally you WANT an infinite loop, so it's not illegal to make one.
- Forgetting indentation, or inconsistent number of spaces in indentation. You HAVE to indent the statements that you want to happen inside the loop (to the same level).

## Break and continue

These two keywords are used as statements. ***break*** ends the loop - execution of the program moves to the line immediately after the loop. ***continue*** ends *this iteration* of the loop - execution of the program moves back to the `while` to test the condition (or to the `for` if this is a `for` loop).

E.g. this version of the counter program uses `continue` to skip iteration 3 - it will print 1,2,4,5:

```python
counter = 0
while counter < 5:
    counter = counter + 1
    if counter == 3:
        continue
    print(counter)
```

E.g. this version of the program uses `break` to stop the loop early if the user requested it via input:

```python
stop = input("Stop at 10? (y/n) ")
counter = 0
while counter < 100:
    counter = counter + 1
    if counter > 10 and stop == "y":
        break
    print(counter)
```

[Return to the site index](index.md)
