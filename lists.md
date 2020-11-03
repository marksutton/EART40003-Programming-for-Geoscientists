Lists
=====

The Python list class is a container class (see [definitions](definitions.md)); 
list objects hold a number of elements, each of which can by any Python objects. 
Lists can hence hold numbers (e.g. 1,3,7 etc), strings ("this","is","a","list"), 
or combinations of these or any other type (e.g. 4.7, 4, True, "text"). 
Lists are ordered, and elements are referred to with an index, i.e. their position in the list 
(starting at 0 not 1). So in the list of four string elements 
"one", "two", "three", "four", the index of the element "three" is 2 
(it's the third element, but we start counting at 0 not at 1, so indices are 0, 1, 2 and 3). 
Lists can be any length, including length 0 – we refer to a list of length 0 as an empty list. 

Python uses square brackets to indicate a list, and elements are separated by commas, 
so lists in your code will look like [1, 2, 10, 20].

Creating lists
-------------

<pre>
my_list = [1, 20, 7]    # Make a list with the elements 1, 20, and 7, in that order
empty_list = []      # Make an empty list (with no elements, ready to have some added later)
</pre>

You can also make an empty list with

<pre>
empty_list = list()      # Make an empty list (with no elements, ready to have some added later)
</pre>

Think of this use of list as if it were a built-in function that makes a list. 
If you give it no argument (as above) it gives you an empty list, but if you give it 
'something list-like' as an argument, it will turn it into an actual list. By 
'something list-like' (and I'm being deliberately vague here), in practice I mean 
either the return result of the range function (see above), or a 'tuple' – 
we'll cover tuples later in the course. So…

<pre>one_to_ten_list = list(range(1,11))  # Make a list [1, 2… 9, 10]
</pre>

*Note for the technically minded! Feel free to ignore this if you don't feel you fall into this category!
Actually what seems to be a list function isn't really a function – it’s a 'constructor' method. All objects (which is everything in Python) have a constructor – a special method that is called when they are created – you call it by using brackets after the class name, hence list(). You can also do things like str() and int() to make empty ints, strings etc. We haven't been doing that because the fundamental Python types like int and str also let you assign values with the more convenient and more readable '=' operator, but a lot of custom classes you may come across don't, so you'll have to create them using the constructor. Most constructors take optional arguments, to set the object up according to some rules. The list constructor knows about things like immutable sequence types and tuples, so you can pass these to it and it will make a list from them – that's what's happening when you do list(range(10)).*

Slicing and indexing
-------------------

List slicing and indexing uses exactly the same syntax as string slicing – see last session's handout.
You use indices in the same way as well (e.g. `my_list[4]` is the 5th item, `mylist[-1]` is the last item).

Method, functions, operators
--------------------------

You can join lists using the + operator, so
<pre>print([1, 2, 4] + [5, 8, 10])  # Prints [1, 2, 4, 5, 8, 10]
</pre>

There are several built-in Python functions that work with lists – see [functions](functions.md) for
some of the more useful ones. For instance len (which works on strings to give the string length)
also works on lists, to give the number of elements, so…

<pre>print(len(["one", "ten", "fifty"]))  # Prints 3 (the length of the list)
</pre>

There are also several useful methods of the list class – see [lists methods](list_methods.md).
Remember that methods use the 'object.' notation, so to use the reverse method…

<pre>
reverse_list = ["one", "ten", "fifty"]	# Set reverse_list to ["one", "ten", "fifty"]
reverse_list.reverse()                      # Reverse it – it will now be ["fifty", "ten", "one"]
</pre>

If at this point you find yourself asking "Why are some things functions and others methods, what's 
the logic in what goes where, and why do there have to be two separate systems"… you are not alone! 
There isn't any hard-and-fast logic in this, although as a rule of thumb most of the functions 
(len, min, max etc) work on many different types of containers (and strings), not just lists, 
while the methods are more list-specific. Not all though, and there are some tasks (like sorting) 
for which both a method and function exist – this can add to the confusion. 
I'm afraid this is just something you have to get used to – Python is not unique in having this
sort of 'two different approaches used at different times' kind of feel to it – this is true of many languages, and reflects their historical 'accretion' as much as anything else. In the end, if you can't remember which way it's meant to be, just Google it, and don't lose sleep over trying to work out why things have to be done in particular ways!

**Common errors with lists**
*	Forgetting the square brackets
*	Getting the start index wrong – it's 0 not 1!
*	Confusing index with element. For instance, the remove method takes an element, the pop method takes an index.
*	Confusing append and extend. Read 'em! 
*	Using methods before creating the list. You can't. If you want to append things onto a list in a loop, you have to make an empty list first.

List Comprehensions
==================

This is where it starts to get a bit complicated. List comprehensions are Python 'shortcuts' which 
combine list creation with loops into a single statement. They are very efficient in terms of the 
amount of typing you have to do – it's very common to want to create a list using a loop, and being 
able to do this in one go with a single line of code is undeniably useful. They are, however, 
rather 'syntactically dense', i.e. difficult to get your head around when you first see them. 
Their use is completely optional in Python - there is nothing that they do that you can't do in other 
ways – but even if you don't use them you ought to be able to recognise and understand them so that
you can understand other people's code. As far as assessment for this module goes, they aren't essential –
but using them well and appropriately is the sort of thing that will get you an extra mark or two. If they 
completely do your head in, then you may be better off just avoiding them as much as possible.
There are also comprehensions for other container types – we'll deal with these later in the course. 
If you don't like list comprehensions, then you are really going to hate dictionary comprehensions. 
Just warning you in advance!

The formal syntax for a list comprehension looks like:

<pre>[expression for item in iterable if condition]
</pre>

This generates a list from iterable, where each element is equal to expression (which can refer to 
item, and usually does). Iterable will normally be an existing list, or a range function. 
The 'if' bit at the end is optional, and is used as a filter – the condition here can also refer to 
item, and typically will. That may make little sense – we need an example.

<pre>
square_numbers = [i**2 for i in range(1,11)]
</pre>

This sets square_numbers to be a list of the first ten square numbers, [1, 4, 9 … 100]. 
Let's break it down. range(1,11) is the iterable in this case – a 'list-like' object 
of numbers 1,2…10. i is the item – this will take the values of the elements in the iterable, 
so 1 for 1st element, 2 for 2nd element, etc. i**2 is the expression – 
this is the value that the corresponding element of the new list will 
actually take (here the value of the range element squared). To clarify what this does, 
a long-hand way of doing the same thing would be:

<pre>square_numbers = []    # set up empty list
for i in range(10)     # loop round 10 times, with i as the loop counter
    square_numbers.append(i)  # add i to the end of the list
</pre>

The expression can be as complex as you like – or it can be really simple. It will normally involve the item, but it doesn't have to. For instance,
 
<pre>ten_zeroes = [0 for i in range(10)]
</pre>

Makes a list consisting of 10 0's, i.e. [0,0,0,0,0,0,0,0,0,0] (Yes, there ARE many good reasons why you might want such a list). Note that even though we aren't using the item in the expression, we still need it in the syntax, and we have to give it a name. A longhand version of this (that does exactly the same thing) would be:

<pre>ten_zeroes = []
for i in range(10)
    square_numbers.append(0)
</pre>

One more example:

<pre>
odd_numbers = [i for i in range(1,100) if i%2 == 1]
</pre>

Here we've included the optional 'if' clause of the comprehension structure. 
Elements are only added to the list if the 'if' condition is True – here it's 
True if the number/2 has a remainder, i.e. if it's odd… so this will only put odd numbers 
into the final list. The longhand version of this is:

<pre>
odd_numbers = []
for i in range(1,100)
    if i%2 == 1:
        odd_numbers.append(i)
</pre>

**Common errors with list comprehensions**
* Using them at all without really understanding what they are doing! I mean it – the first few times you use one, think very carefully about what goes where.
* Not putting an expression in – you have to have an expression, an item, and an iterable. Only the 'if' part is optional.
