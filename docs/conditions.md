# Conditions

Conditions are expressions that Python can evaluate to 'True' or 'False', and are used in a) [if / elif / else blocks](if.md), and b) [while loops](while.md).

## 1. True or False values

Simplest type of condition: just a True or False value. Note True and False have an initial capital letter in Python. These aren't very practical, though occasionally a while loop that never ends because of the condition is useful (as you can also exit it with a `break` statement if you need to).

<div class="syntax-template" style="font-family:inherit; background:#f4f7fa; border-left:3px solid #5483bc; padding:0.5em 0.8em; margin:0.8em 0">
<p style="margin:0"><strong>while True:</strong></p>
<p style="margin:0">    [Code to keep looping over forever]</p>
</div>


## 2. Comparison operators

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

## 3. Compound conditions

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

## Common errors

- Using a single equals sign. Single equals assigns values to variables. Use double equals for comparisons.
- Missing off the variable name in second condition of an and/or. This is a very common 'rookie' error, because in English, **`a>10 or <0`** makes perfect sense. It doesn't to Python! You need **`a > 10 or a < 0`**.
- Misunderstanding order of evaluation of complex conditions - see above - use brackets to control it, don't assume you know which order things happen in.
- Mixing types in an illegal way, e.g. **`a < 5`** is illegal if *a* is a string.
- Trying to do precise (`==` or `!=`) comparisons with floating point (i.e. non-integer) numbers. These don't always work. This is a counterintuitive and complex issue, which we will cover properly next week. Ignore for now... but keep it at the back of your mind.

[Return to the site index](index.md)
