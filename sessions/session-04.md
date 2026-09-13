---
course: EART40003
course_title: Programming for Geoscientists
session: 4
year: 2026
author_short: MDS
title: "Session 4: Reference"
subtitle: "Reference and pre-reading"
---

# Definitions

### Container (or container class, or collections class, or iterable – for the purposes of this course you can treat these as meaning the same thing)

An object comprising multiple *elements*. The most obvious and useful example in Python is the *list* class – lists contain a number of elements in some defined order, referred to by their index number. Other containers exist (sets, dictionaries and tuples are the most encountered ones – not dealt with this week – plus an odd list-like one that is returned by the *range* function – see below)

### Iterable

A Python term for anything that can be *iterated* over – in practice, this is much the same thing as a *container*.

### Element

an individual item in a *container*.

### Iterating

looping. We often talk about 'iterating over a list', which means executing a loop to look at each element in turn.

### Comprehension

A Python term for a syntax-construction that enables you to do certain container iteration tasks with very little typing. See syntax section below for list comprehensions. Depending on who you ask, comprehensions are either wonderful labour-saving constructions that make everyone's life easier, or hellish syntactical minefields that wreck code-readability and hamper debugging.

### List

A simple type of *container* class. See syntax section below for details of Python lists.

### Array

A simple type of *container* not actually available in Python (though see Numpy arrays in session 7), but commonly used in other languages. Arrays are a bit like lists, but (a) often have a fixed number of elements, and (b) normally require all elements to be of the same type.

# Functions

### `len(container)`

**Returns:** int  
**Origin:** built-in  

The len function, which we have seen used on strings, also works on containers such as lists – it returns the number of elements.

### `min(container)`

**Returns:** varies  
**Origin:** built-in  

Use on any container (e.g. a list) to find the minimum value. Works on numerical and string elements – for string elements, it will give you the alphabetically first value.

### `max(container)`

**Returns:** varies  
**Origin:** built-in  

Use on any container (e.g. a list) to find the maximum value. Works on numerical and string elements – for string elements, it will give you the alphabetically last value.

### `range(start, stop, [step])`

**Returns:** weird list-like thing of ints  
**Origin:** built-in  

Generates an iterable/container thing (like a list, but actually not a list) containing integers between *start* and *stop* (but not including stop), advancing in *step* increments. *Step* is an optional argument – if you omit it, *step* is 1. So **range(1,5)** gives you [**1,2,3,4]** and **range (1,10,3)** gives you **[1,4,7]**. If you use range with only ONE argument, that argument is treated as a stop value and the implicit start is 0, so **range(5)** represents the values **[0,1,2,3,4]**. IMPORTANT: *range* does NOT return a list. Some websites may tell you it does (and it did in older versions of Python), but actually in Python 3 it returns a quirky thing called an "immutable sequence type", which you are probably not going to come across in any other context. It’s a bit like a list – but not quite a list. This return value *is* an 'iterable' at least, so the for loop construction works fine with it - e.g. **for i in range(0,5):**. It is legal to print a range object, but this does not print its contained values as though it were a list: in the course Python 3.14 environment, **print(range(5))** displays a representation such as **range(5)**. If you want the actual values as a list, use **list(range(...))**, so e.g. **list_0_to_10 = list(range(0,11))** works.

### `sum(container)`

**Returns:** number  
**Origin:** built-in  

Use on any container (e.g. a list) to find the sum of all values in the container. Works on numerical but not string elements.

# Methods

### `list (built-in container class)`

These are methods not functions, so the syntax uses the ‘.’ after an object of type list. For example, use **mylist.sort()** not **sort(mylist)** to sort the elements of a list into order.

Note that unlike string methods, **many of these don't just return a new modified copy of the list** – they modify the original list in-place (and typically don't return anything). See descriptions.

#### `append(value)`

**Returns:** N/A  

Appends *value* to the end of the list. *Value* can be any valid Python object. Note that if you want to add another list to the end of this list, don't use *append*, which will create a single extra element of type list! Use *extend* instead, or add the lists with the + operator.<br>*append* modifies the list in-place, so doesn't return anything.

#### `count(element)`

**Returns:** int  

Counts how many times the element *element* occurs in the list, returning an integer. So **[1,2,2,3,4,3,2,4,1,4,1].count(1)** returns 3.

#### `extend(newlist)`

**Returns:** N/A  

Adds the elements of *newlist* to the end of this list. *Extend* modifies the list in-place, so doesn't return anything.

#### `insert(index, element)`

**Returns:** N/A  

Inserts a new element into the list at position *index*.

#### `pop(index)`

**Returns:** varies  

Removes the element at position *index* from the list, and returns it. Note that this is different from *remove*, which needs the value of the element, not the index number (and doesn't return anything).

#### `remove(element)`

**Returns:** N/A  

Removes *element* from the list – note that this takes an element, not an index number (use *pop* instead if you want to do that). If the element doesn't exist, an exception is thrown.

#### `reverse()`

**Returns:** N/A  

Reverses the order of the list. Affects the list in-place, so doesn't return anything.

#### `sort()`

**Returns:** N/A  

Sorts the list in-place, into numerical or alphabetical order. Does not return anything. NOTE – there IS also a sorted function (not a method) that does much the same thing.

### `str (built-in string class)`

These are methods not functions, so the syntax uses the ‘.’ after an object of type str. For example, use **",".join(mylist)** not **join(mylist,",")**. Some string methods have already been given – those below are the new ones introduced today (that involve lists)

#### `split(split_on)`

**Returns:** list (of strings)  

Splits a string on the substring *split_on* into a list of strings. For example, **"goodbye cruel world".split(" ")** returns **["goodbye", "cruel", "world"]**. *split_on* is normally one a one-character string, but it doesn't have to be.

#### `join(container)`

**Returns:** string  

The opposite of *split*. Join takes a container (e.g. a list, normally a list of strings) as an argument and joins all the elements together into a single string, using the object string as a separator. For example, **",".join(["goodbye", "cruel", "world"])** returns the string **"goodbye,cruel,world".**

# Topics

## Breaking up long lines

Sometimes your lines will get too long (the linter will complain, and it IS best to avoid them). You can break lines with \ like so:

```python
variable_with_a_possibly_over_verbose_name =\
      not_quite_so_verbose_variable_name * 2
```

Or inside brackets, or square brackets, you can just put a line break in without worrying, e.g.

```python
result = (first_value * second_value
          + third_value / fourth_value)
```

If you do this, linters like the continuation to line up with the first character under the bracket on the line above. Breaking lines that contain long strings is harder. If you have:

```python
print("this is a very very very very very very very very very very very very very long string")
```

Your options are:

```python
print("this is a very very very very very very very "
      + "very very very very very very very very very "
      + "very very long string")
```

Or the version below – if there are two strings next to each other without a plus, python just joins them anyway

```python
print("this is a very very very very very very very "
      "very very very very very very very very very "
      "very very long string")
```

## Lists

The Python list class is a container class (see above); list objects hold a number of *elements*, each of which can be any Python object. Lists can hence hold numbers (e.g. 1,3,7 etc), strings ("this","is","a","list"), or combinations of these or any other type (e.g. 4.7, 4, True, "text"). Lists are ordered, and elements are referred to with an *index*, i.e. their position in the list (starting at 0 not 1). So in the list of four string elements "one", "two", "three", "four", the index of the element "three" is 2 (it's the third element, but we start counting at 0 not at 1, so indices are 0, 1, 2 and 3). Lists can be any length, including length 0 – we refer to a list of length 0 as an empty list.

Python uses square brackets to indicate a list, and elements are separated by commas, so lists in your code will look like [1, 2, 10, 20].

### Creating lists

```python
my_list = [1, 20, 7]    # Make a list with the elements 1, 20, and 7, in that order
empty_list = []      # Make an empty list (with no elements, ready to have some added later)
```

You can also make an empty list with

```python
empty_list = list()      # Make an empty list (with no elements, ready to have some added later)
```

Think of this use of *list* as if it were a built-in function that makes a list\*. If you give it no argument (as above) it gives you an empty list, but if you give it 'something list-like' as an argument, it will turn it into an actual list. By 'something list-like' (and I'm being deliberately vague here), in practice I mean either the return result of the range function (see above), or a 'tuple' – we'll cover tuples later in the course. So…

```python
one_to_ten_list = list(range(1,11))  # Make a list [1, 2… 9, 10]
```

> **Technical note — optional:** Feel free to ignore this if you don't feel technically minded!
>
> Actually, what seems to be a list function isn't really a function – it’s a 'constructor' method. All objects (which is everything in Python) have a constructor – a special method that is called when they are created – you call it by using brackets after the class name, hence list(). You can also do things like str() and int() to make empty ints, strings etc. We haven't been doing that because the fundamental Python types like int and str also let you assign values with the more convenient and more readable '=' operator, but a lot of custom classes you may come across don't, so you'll have to create them using the constructor. Most constructors take optional arguments, to set the object up according to some rules. The list constructor knows about things like immutable sequence types and tuples, so you can pass these to it and it will make a list from them – that's what's happening when you do list(range(10)).

## Slicing and indexing

List slicing and indexing uses *the same* syntax as string slicing – see last session's handout. You use indices in the same way as well (e.g. `my_list[4]` is the 5<sup>th</sup> item, `mylist[-1]` is the last item).

### Method, functions, operators

You can join lists using the + operator, so

```python
print([1, 2, 4] + [5, 8, 10])  # Prints [1, 2, 4, 5, 8, 10]
```

There are several built-in Python functions that work with lists – see above for some of the more useful ones. For instance *len* (which works on strings to give the string length) also works on lists, to give the number of elements, so…

```python
print(len(["one", "ten", "fifty"]))  # Prints 3 (the length of the list)
```

There are also several useful methods of the list class – also see above. Remember that methods use the 'object.' notation, so to use the *reverse* method…

```python
reverse_list = ["one", "ten", "fifty"]	# Set reverse_list to ["one", "ten", "fifty"]
reverse_list.reverse()                 # Reverse it – it will now be ["fifty", "ten", "one"]
```

If at this point you find yourself asking "Why are some things functions and others methods, what's the logic in what goes where, and why do there have to be two separate systems"… you are not alone! There isn't any hard-and-fast logic in this, although as a rule of thumb most of the functions (len, min, max etc) work on many different types of containers (and strings), not just lists, while the methods are more list-specific. Not all though, and there are *some* tasks (like sorting) for which both a method and function exist – this can add to the confusion. I'm afraid this is just something you have to get used to – Python is not unique in having this sort of 'two different approaches used at different times' kind of feel to it – this is true of many languages, and reflects their historical 'accretion' as much as anything else. In the end, if you can't remember which way it's meant to be, just Google it, and don't lose sleep over trying to work out *why* things have to be done in particular ways!

List comprehensions are another part of list syntax – these are deliberately separated out here and moved to the end of this document, as you'll need to understand *for* loops before thinking about them.

### Common errors

- Forgetting the square brackets

- Getting the start index wrong – it's 0 not 1!

- Confusing index with element. For instance, the *remove* method takes an element, the pop method takes an index.

- Confusing append and extend. Read the details – they are not the same thing.

- Using methods before creating the list. You can't. If you want to append things onto a list in a loop, you have to make an empty list first.

## 'in' in conditions

A nice simple feature! You can use the keyword *in* to find out whether an element is in a list (or in any type of container class). The condition:

::: syntax-template

*check_element* **in** *container*

:::

is True if there is one or more element in *container* matching the *check_element*. e.g.

```python
if "one" in number_list:
    print("'One' found in the list")
```

## For loops

One of the more refreshingly simple things about Python is that it only has two types of loops (some languages have a whole profusion of them). We have already seen *while* loops - *for* loops are the other Python loop-type. *for* loops are used for iterating (looping) over 'iterables' – which are containers with multiple values, like lists. As such they are a little more specialised than the general-purpose *while* loops, but are nonetheless even more commonly used. Their syntax is:

::: syntax-template

for item in iterable:

    [one or more lines to execute each time round loop]

:::

This will loop round as many times as there are elements in the *iterable* container object (which is often going to be a list). The first time round the loop, the variable *item* will have the value of the first element. The second time, it will have the value of the second element… etc. For example…

```python
my_list = [1,10,100]
for number in my_list:
    print(number)
```

… will print 1, 10 and 100. While technically what a *for* loop does is iterate over an iterable, in practice you can also use it to just loop a certain number of times. In earlier sessions, you will recall that we have built counter loops using 'while' to do that  – we set a counter to 0, our *while* condition checked the counter to see if it had reached a desired maximum, and each time round the loop we added 1 to it. This worked fine and was good practice (NOT a waste of time!), but *for* loops in conjunction with the *range* function provide a more efficient way to do this.

The range function (see above) is used to make sequences of integers, and returns something that's 'almost but not quite a list'. See above for details. This slightly odd 'list-like thing' that it returns is an iterable, i.e. you can use *for* loops on it – in fact getting used in *for* loops is the most important purpose of the *range* function. So…

::: syntax-template

for number in range(10):   # loop 10 times, number set to values 0, 1… 9

    [do stuff]

:::

Does the same as the code below, but is much more concise

::: syntax-template

number = 0
while number<10:

    [do stuff]

    number += 1

:::

### Common errors

- Forgetting the : at the end

- Using the range stop value incorrectly – remember that range(0, 10) generates 0-9, not 0-10.

- Forgetting to indent. This is not optional!

- Getting confused with *while*. If you put a condition in a for loop it doesn't work! It needs an item name, and a container/iterable name.

## List comprehensions

This is where it starts to get a bit complicated. List comprehensions are Python 'shortcuts' which combine list creation with loops into a single statement. They are very efficient in terms of the amount of typing you have to do – it's very common to want to create a list using a loop, and being able to do this in one go with a single line of code is undeniably useful. They are, however, rather 'syntactically dense', i.e. difficult to get your head around when you first see them. Their use is completely optional in Python - there is nothing that they do that you can't do in other ways – but even if you don't use them you ought to be able to recognise and understand them so that you can understand other people's code. As far as assessment for this module goes, they aren't essential – but using them well and appropriately is the sort of thing that will get you an extra mark or two. If they completely do your head in, then you may be better off just avoiding them as much as possible.

There are also comprehensions for other container types – we'll deal with these later in the course. If you don't like list comprehensions, then you are *really* going to hate dictionary comprehensions. Just warning you in advance!

The formal syntax for a list comprehension looks like:

::: syntax-template

[expression for item in iterable if condition]

:::

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

### Common errors

- Using them at all without really understanding what they are doing! I mean it – the first few times you use one, think **very** carefully about what goes where.

- Not putting an expression in – you have to have an expression, an item, and an iterable. Only the 'if' part is optional.

# Exercises

These will check you understand lists, for loops, and list comprehensions. For each, what will the code-snippet print? The last two are meant to be hard!

| Code | Prints? |
| --- | --- |
| `my_list = [1, 3, 5, 7]`<br>`print(my_list[2])` |  |
| `print([1, 3, 5, 7, 9][2:4])` |  |
| `listy_mc_listface = [1, 10, 100]`<br>`for i in listy_mc_listface:`<br>`    print(i * 10)` |  |
| `print([x + 7 for x in range(5)])` |  |
| `numbers = []`<br>`for i in range(10,20,2):`<br>`    numbers.append(i*2)`<br>`print(sum(numbers[-3:]))` |  |
| `print([str(x)+"0" for x in range(1,20) if`<br>`       len(str(x*4))<=2].reverse())` |  |
