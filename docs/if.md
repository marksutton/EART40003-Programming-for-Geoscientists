# If / elif / else

In Python, these three keywords provide all conditional program flow functionality. They are used together, in an *if block*. An *if block* begins with an `if` statement, followed by indented lines of code to be executed if the condition is True. Optionally, it can also have one or more `elif` statements (`elif` is short for *else if*, though if you type *else if* Python won't understand it) plus associated indented lines of code. These are used to catch alternative conditions, Finally, optionally again, you can have one `else` statement and associated code, to catch any cases not caught already. Crucially, at most only ONE block of indented code is executed each time the program runs through an entire if/elif/else block. *See [Conditions](conditions.md) for more on conditions*.

<div class="syntax-template" style="font-family:inherit; background:#f4f7fa; border-left:3px solid #5483bc; padding:0.5em 0.8em; margin:0.8em 0">
<p style="margin:0"><strong>if <em>condition1</em>:</strong></p>
<p style="margin:0">    Code to execute if condition1 was True (can be as many lines as
needed)</p>
<p style="margin:0"><strong>elif <em>condition2</em>:</strong> [elif blocks are
optional]</p>
<p style="margin:0">    Code to execute if condition2 was True and condition1 was false
(can be as many lines as needed)</p>
<p style="margin:0"><strong>elif <em>condition3</em>:</strong> [elif blocks are
optional]</p>
<p style="margin:0">    Code to execute if condition3 was True and both condition1 and
condition 2 were false</p>
<p style="margin:0">… [as many elif blocks as you like]</p>
<p style="margin:0"><strong>else:</strong> [else block is optional]</p>
<p style="margin:0">    Code to execute if none of the if or elif conditions were
True</p>
</div>


## Common errors

- Forgetting the colon (`:`) at the end of the `if` / `elif` / `else` line. This is required.
- Forgetting to indent. Python absolutely needs indents to tell it which statements are in which block.
- Unreachable blocks. For instance, if your `if` condition is `a > 5`, an `elif` block with a condition of `a > 10` will never be executed - if `a > 10` it's also `> 5`, so the initial `if` block will run, not the `elif` block.
- Condition errors - see [Conditions](conditions.md).

## Example 1 — Simple `if` check to warn if a value is too large

```python
if a > 1000:
    print("Warning - a is very large - results may be inaccurate")
```

## Example 2 — Check whether a value is in the expected range

```python
if a > 1000 or a < 0:
    print("Warning - a is outside expected range of 0-1000")
else:
    print("Information - a is in normal range")
```

## Example 3 — Keep a value within the range 0–5

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

[Return to the site index](index.md)
