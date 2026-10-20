# For loops

One of the more refreshingly simple things about Python is that it only has two types of loops (some languages have a whole profusion of them). We have already seen [*while* loops](while.md) - *for* loops are the other Python loop-type. *for* loops are used for iterating (looping) over 'iterables' – which are containers with multiple values, like lists. As such they are a little more specialised than the general-purpose *while* loops, but are nonetheless even more commonly used. Their syntax is:

<div class="syntax-template" style="font-family:inherit; background:#f4f7fa; border-left:3px solid #5483bc; padding:0.5em 0.8em; margin:0.8em 0">
<p style="margin:0">for item in iterable:</p>
<p style="margin:0">    [one or more lines to execute each time round loop]</p>
</div>


This will loop round as many times as there are elements in the *iterable* container object (which is often going to be a list). The first time round the loop, the variable *item* will have the value of the first element. The second time, it will have the value of the second element… etc. For example…

```python
my_list = [1,10,100]
for number in my_list:
    print(number)
```

… will print 1, 10 and 100. While technically what a *for* loop does is iterate over an iterable, in practice you can also use it to just loop a certain number of times. In earlier sessions, you will recall that we have built counter loops using 'while' to do that  – we set a counter to 0, our *while* condition checked the counter to see if it had reached a desired maximum, and each time round the loop we added 1 to it. This worked fine and was good practice (NOT a waste of time!), but *for* loops in conjunction with the *range* function provide a more efficient way to do this.

The [range function](functions.md#rangestart-stop-step) is used to make sequences of integers, and returns something that's 'almost but not quite a list'. See [range()](functions.md#rangestart-stop-step) for details. This slightly odd 'list-like thing' that it returns is an iterable, i.e. you can use *for* loops on it – in fact getting used in *for* loops is the most important purpose of the *range* function. So…

<div class="syntax-template" style="font-family:inherit; background:#f4f7fa; border-left:3px solid #5483bc; padding:0.5em 0.8em; margin:0.8em 0">
<p style="margin:0">for number in range(10): # loop 10 times, number set to values 0, 1…
9</p>
<p style="margin:0">    [do stuff]</p>
</div>


Does the same as the code below, but is much more concise

<div class="syntax-template" style="font-family:inherit; background:#f4f7fa; border-left:3px solid #5483bc; padding:0.5em 0.8em; margin:0.8em 0">
<p style="margin:0">number = 0<br />
while number&lt;10:</p>
<p style="margin:0">    [do stuff]</p>
<p style="margin:0">    number += 1</p>
</div>


## Common errors

- Forgetting the : at the end

- Using the range stop value incorrectly – remember that range(0, 10) generates 0-9, not 0-10.

- Forgetting to indent. This is not optional!

- Getting confused with *while*. If you put a condition in a for loop it doesn't work! It needs an item name, and a container/iterable name.

For early loop termination or skipping an iteration, see [Break and continue](while.md#break-and-continue).

[Return to the site index](index.md)
