---
course: EART40003
course_title: Programming for Geoscientists
session: 2
year: 2026
author_short: MDS
title: "Session 2: Reference"
subtitle: "Pre-session reading & exercise (see last page)"
header_title: "Session 2 - Reference"
---

# Definitions

### Condition

Something that a programming language can evaluate to a *Boolean* value (a True or False), and hence use as the basis of a decision that affects program flow.

### Boolean

A Boolean value (named after the mathematician George Boole) is one that can only have one of two values, normally expressed as True or False.

### Debugger

A debugger (properly symbolic debugger) is a piece of software that enables a programmer to step through a program line-at-a-time, watching variable values, and following exactly what their program is doing. This is not the only way to debug a program, but is often the easiest way. Debuggers can either be set to step through programs when the user presses a key, or to run the program as normal (full-speed mode) until it reaches a predefined point (a *breakpoint*).

### Breakpoint

See *Debugger*. A point set in a program to force the debugger to stop running at full speed and enter line-at-a-time mode.

### Nesting

Putting a program structure inside another program structure. Pretty well anything can be nested in programming, including function calls, if statements, loops etc. Nesting takes two forms in Python. Nesting within expressions - e.g. `float(input("hello"))` - consists of brackets within brackets (innermost always happens first). Nesting of control structures (`if`, `while` etc.) is done using indentation. Most languages encourage this indentation for readability, but in Python it is mandatory.

# Functions

### `int(value)`

**Returns:** integer  
**Origin:** built-in

Takes a value and tries to convert it into an integer (i.e. a whole number). Normally used to convert a string containing an integer (e.g. from an `input` function) into a number for calculation, but it can also convert a floating-point number such as `2.5` into an integer. When converting a floating-point number, `int` **truncates towards zero**: for example, `int(3.9)` gives `3`, while `int(-5.8)` gives `-5`. This is not the same as rounding to the nearest integer; use `round()` if that is what you need. If a value cannot be converted, `int` throws an error and stops the program. For example, the string `"4"` can be converted, but `"4.5"` and `"Forty-two"` cannot.

# Topics

## If / elif / else

In Python, these three keywords provide all conditional program flow functionality. They are used together, in an *if block*. An *if block* begins with an `if` statement, followed by indented lines of code to be executed if the condition is True. Optionally, it can also have one or more `elif` statements (`elif` is short for *else if*, though if you type *else if* Python won't understand it) plus associated indented lines of code. These are used to catch alternative conditions, Finally, optionally again, you can have one `else` statement and associated code, to catch any cases not caught already. Crucially, at most only ONE block of indented code is executed each time the program runs through an entire if/elif/else block. *See below for more on conditions*.

::: syntax-template

**if *condition1*:**

    Code to execute if condition1 was True (can be as many lines as needed)

**elif *condition2*:**  [elif blocks are optional]

    Code to execute if condition2 was True and condition1 was false (can be as many lines as needed)

**elif *condition3*:**  [elif blocks are optional]

    Code to execute if condition3 was True and both condition1 and condition 2 were false

... [as many elif blocks as you like]

**else:**  [else block is optional]

    Code to execute if none of the if or elif conditions were True

:::

### Common errors

- Forgetting the colon (`:`) at the end of the `if` / `elif` / `else` line. This is required.
- Forgetting to indent. Python absolutely needs indents to tell it which statements are in which block.
- Unreachable blocks. For instance, if your `if` condition is `a > 5`, an `elif` block with a condition of `a > 10` will never be executed - if `a > 10` it's also `> 5`, so the initial `if` block will run, not the `elif` block.
- Condition errors - see conditions section.

### Example 1 — Simple `if` check to warn if a value is too large

```python
if a > 1000:
    print("Warning - a is very large - results may be inaccurate")
```

### Example 2 — Check whether a value is in the expected range

```python
if a > 1000 or a < 0:
    print("Warning - a is outside expected range of 0-1000")
else:
    print("Information - a is in normal range")
```

### Example 3 — Keep a value within the range 0–5

```python
if a > 5:
    print("a was too big, setting it to 5")
    a = 5
elif a < 0:
    print("a was too small, setting it to 0")
    a = 0
else:
    print("a was in correct range 0-5")
```

## While loops

Loops - code blocks executed repeatedly - are fundamental to most non-trivial programs. Python has two types of loops - `while` loops, and `for` loops (we will cover `for` loops later). `while` loops are very simple in concept, and are general-purpose loops. They begin with a `while` statement that contains a condition, which is followed by one or more lines of code to be executed repeatedly, as long as the condition continues to be true. This code has to be indented to tell Python which lines are within the while block.

::: syntax-template

**while *condition*:**

    Code to execute as long as condition is True (can be as many lines as needed)

:::

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

Your condition doesn't have to use a counter - it can be any legal condition (see below for more on conditions). You could for instance put an input statement inside a loop, and keep going round until the user types in a number that is within a certain range.

See *break and continue* below for some ways to do more subtle loop control within a `while` loop.

### Common errors

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

## Conditions

Conditions are expressions that Python can evaluate to 'True' or 'False', and are used in a) if / elif / else blocks, and b) while loops.

### 1. True or False values

Simplest type of condition: just a True or False value. Note True and False have an initial capital letter in Python. These aren't very practical, though occasionally a while loop that never ends because of the condition is useful (as you can also exit it with a `break` statement if you need to).

::: syntax-template

**while True:**

    [Code to keep looping over forever]

:::

### 2. Comparison operators

More common type: using a comparison operator (e.g. `if a > 10:`). Comparison operators available are:

- `>`, `<` — greater than, less than. **In this course, we will use these with numbers.**
- `>=`, `<=` — greater than or equal to, less than or equal to. **In this course, we will use these with numbers.**
- `==`, `!=` - equal to, not equal to. Can use on any types (including strings).

| Condition | Meaning |
|---|---|
| `a > 10` | True if a is more than 10, False if a is 10 or lower |
| `b <= 10` | True if b is 10 or less, False if b is higher than 10 |
| `a == b` | True if the values of a and b are precisely equal, otherwise False. Note two = signs! |
| `a != "cat"` | False if the string variable a is **"cat"**, True if it is *anything* else. Note that string comparisons are case sensitive - if a holds **"Cat"** then the condition evaluates to True. |

### 3. Compound conditions

Often you want more complex conditions. To construct these, use the *and* and *or* 'Boolean operators', e.g. `if a > 10 and b > 10:`

`and` - both of the conditions need to be True  
`or` - one (or both) of the conditions need to be True

So if a is 5, b is 15:

`a > 10 and b > 10` is False (only one of the conditions is True)

`a > 10 or b > 10` is True (only one of the conditions is True, that's enough for 'or')

You can chain these together to make even more complex conditions, but always use brackets to make sure you control the order (the most deeply nested brackets are calculated first). It can make a difference.

Consider:

`(a > 10 and b < 10) or b > 13`

This is True. Neither condition in the 'and' bit in brackets is True, so that evaluates to False - but b IS greater than 13, so the 'or' bit, done last, is True, and the overall expression is True.

`a > 10 and (b < 10 or b > 13)`

Here the brackets have moved so the 'or' gets done first. b is > 13 so the bracket evaluates to True, but a > 10 is False so the final 'and' evaluates to False, and the overall expression is False.

Finally (but less commonly useful) there is also a *not* Boolean operator, which flips True=>False and False=>True. So:

| Condition | Meaning |
|---|---|
| `not (a > 10)` | False if a is more than 10, True if a is 10 or lower |
| `not (a == b)` | False if the values of a and b are precisely equal, otherwise True. This is precisely equivalent to `a != b`. |

### Common errors

- Using a single equals sign. Single equals assigns values to variables. Use double equals for comparisons.
- Missing off the variable name in second condition of an and/or. This is a very common 'rookie' error, because in English, **`a>10 or <0`** makes perfect sense. It doesn't to Python! You need **`a > 10 or a < 0`**.
- Misunderstanding order of evaluation of complex conditions - see above - use brackets to control it, don't assume you know which order things happen in.
- Mixing types in an illegal way, e.g. **`a < 5`** is illegal if *a* is a string.
- Trying to do precise (`==` or `!=`) comparisons with floating point (i.e. non-integer) numbers. These don't always work. This is a counterintuitive and complex issue, which we will cover properly next week. Ignore for now... but keep it at the back of your mind.

# Exercises

## Conditions exercise (try before Session 2)

**Before class, work through these and write in either True or False (or Illegal if you think the condition is miscoded and would throw an error).**

For all these, variable values are: **`a = 5`, `b = 15`, `c = -2.3`, `d = "cat"`, `e = "dog"`.**

| Condition | True/False/Illegal | Condition | True/False/Illegal |
|---|:---:|---|:---:|
| `a > 10` | | `a >= 5 or (c > 0 and d != "cat")` | |
| `b != a` | | | |
| `c <= d` | | `a == 5 and (c == "Cat" or d == "Cat")` | |
| `c >= b` | | | |
| `a > 5 or b > 15` | | `not (c < 0 or a != 5)` | |
| `a < 10 or > 0` | | | |
| `b > 100 or b > a` | | `not ((a > 10 or a < 0) and (not (b == 15 or a == 15)))` | |
| `not (c = d)` | | | |
| `not (a != b)` | | | |
