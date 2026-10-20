# List comprehensions

This is where it starts to get a bit complicated. List comprehensions are Python 'shortcuts' which combine list creation with loops into a single statement. They are very efficient in terms of the amount of typing you have to do – it's very common to want to create a list using a loop, and being able to do this in one go with a single line of code is undeniably useful. They are, however, rather 'syntactically dense', i.e. difficult to get your head around when you first see them. Their use is completely optional in Python - there is nothing that they do that you can't do in other ways – but even if you don't use them you ought to be able to recognise and understand them so that you can understand other people's code. As far as assessment for this module goes, they aren't essential – but using them well and appropriately is the sort of thing that will get you an extra mark or two. If they completely do your head in, then you may be better off just avoiding them as much as possible.

There are also comprehensions for other container types – we'll deal with these later in the course. If you don't like list comprehensions, then you are *really* going to hate dictionary comprehensions. Just warning you in advance!

See [For loops](for.md) for the loop syntax used here.

The formal syntax for a list comprehension looks like:

<div class="syntax-template" style="font-family:inherit; background:#f4f7fa; border-left:3px solid #5483bc; padding:0.5em 0.8em; margin:0.8em 0">
<p style="margin:0">[expression for item in iterable if condition]</p>
</div>


This generates a list from *iterable*, where each element is equal to *expression* (which can refer to *item*, and usually does). *Iterable* will normally be an existing list, or a range function. The 'if' bit at the end is optional, and is used as a filter – the condition here can also refer to *item*, and typically will. That may make little sense – we need an example.

```python
square_numbers = [i**2 for i in range(1,11)]
```

This sets *square_numbers* to be a list of the first ten square numbers, [1, 4, 9 … 100]. Let's break it down. *range(1,11)* is the *iterable* in this case – a 'list-like' object of numbers 1,2…10. i is the *item* – this will take the values of the elements in the iterable, so 1 for 1<sup>st</sup> element, 2 for 2<sup>nd</sup> element, etc. *i\*\*2* is the *expression* – this is the value that the corresponding element of the new list will actually take (here the value of the range element squared). To clarify what this does, a long-hand way of doing the same thing would be:

```python
square_numbers = []    # set up empty list
for i in range(1,11):  # loop over 1 to 10, with i as the loop counter
    square_numbers.append(i**2)  # add i squared to the end of the list
```

The expression can be as complex as you like – or it can be simple. It will normally involve the *item*, but it doesn't have to. For instance,

```python
ten_zeroes = [0 for i in range(10)]
```

Makes a list consisting of 10 0's, i.e. [0,0,0,0,0,0,0,0,0,0] (Yes, there ARE many good reasons why you might want such a list). Note that even though we aren't using the *item* in the expression, we still need it in the syntax, and we must give it a name. A longhand version of this (that does the same thing) would be:

```python
ten_zeroes = []
for i in range(10):
    ten_zeroes.append(0)
```

One more example:

```python
odd_numbers = [i for i in range(1,100) if i%2 == 1]
```

Here we've included the optional 'if' clause of the comprehension structure. Elements are only added to the list if the 'if' condition is True – here it's True if the number/2 has a remainder, i.e. if it's odd… so this will only put odd numbers into the final list. The longhand version of this is:

```python
odd_numbers = []
for i in range(1,100):
    if i%2 == 1:
        odd_numbers.append(i)
```

## Common errors

- Using them at all without really understanding what they are doing! I mean it – the first few times you use one, think **very** carefully about what goes where.

- Not putting an expression in – you have to have an expression, an item, and an iterable. Only the 'if' part is optional.

[Return to the site index](index.md)
