Dictionaries
=============

Dictionaries are another type of container class (= iterables, collections). See definitions section. A good way to think about them is as look-up tables. 
Dictionaries don't have indices like lists – instead they have 'keys', which are much more flexible. Dictionaries can be set up in code like lists, 
except that they use curly brackets { } instead of square brackets [ ]. For example:
 
<pre>digit_dict = {"one":1, "two":2, "three":3, "four":4, "five":5,
      "six":6, "seven":7, "eight":8, "nine":9}
</pre>

Notice that the each item has two pieces of data – the first (before the colon) is the key, and the second is the value, or element.
Notice also that I split the line – you are allowed to do this without a \ inside curly brackets (or any brackets for that matter).
Keys are used like indices to look up elements, so

<pre>print(digit_dict["two"])   # prints 2
</pre?

Perhaps slightly confusingly, Python still uses square brackets to look things up in dictionaries, just like indexing in arrays. 
It might have made more sense if they used curly brackets, but they didn't. Curly brackets are only used for defining 'pre-made' dictionaries in code.

Keys can be any type – here they are strings, but they could instead be numbers. They COULD be other types, but that's rarely a good idea. 
They also don't all have to be the same type in any given dictionary, but (again) that's unlikely to be what you really want. 
Elements can of course also be any type – that includes other collections like lists and dictionaries. Y
ou are allowed to have different element types as values in one dictionary, but (once more) it's probably not a good idea. 
99% of the time you'll want to use dictionaries where all the keys are of one type, either numbers or strings, 
and all the elements are of one type as well (which could be just about anything).

Keys must be unique – you can't have two keys the same. If you set the value for a key twice, the second value replaces the first. 
This is one way in which keys work exactly like list indices. 

You can iterate over dictionaries using for loops, but what you are iterating over is the keys, not the values. This isn't a problem, unless you expect it to be the values! So…

<pre>for i in digit_dict:
    print(i)
</pre>

prints "one", "two" … "nine" (the keys). If you want to print the values, just look them up in the dictionary – so use

<pre>
for i in digit_dict:
    print(digit_dict[i])
</pre>

which prints 1,2 … 9

Methods
-------

See the [methods section](dict_methods.md) for a list of useful methods. The most important is probably 
update, which adds an entire new dictionary to the first, but can also be used to add single items, like so:

<pre>digit_dict.update({"ten": 10})  # add another key/value pair to digit_dict
</pre>

Note that this needs the curly brackets, as what you are actually doing is making a new dictionary (here of length 1) and then adding it to the original one.

You CAN also add single new items in a more direct way...

<pre>digit_dict["ten"] = 10
</pre>

To remove items use `pop(key)`. To get a list of the values, use `values()`, and to get a list of the keys, use `keys()`

Note – there ARE such things as dictionary comprehensions. If you feel brave, look ‘em up! I won’t be teaching them in this course.

Differences between dictionaries and lists
---------------------------------------

Dictionaries are 'unordered' – the key/value pairs are not stored in any particular order, and if you expect them to be in order when you 
iterate with for you may run into trouble. This also means that there is no 'slicing' syntax (slicing makes no sense for an unordered container).

Some of the Python functions that work on lists also work on dictionaries. 
len does what you expect (gives you the number of key/value pairs). 
max, min and sum also work, but they work on the keys not the values, which is probably not what you expect. 

You can use `in` in a condition just like in a list – but (again) it's the keys not the values that are searched.

You can't add dictionaries with +. Use the update method instead

Common errors with dictionaries
*	Not being aware of whether a particular object in your code is a dictionary or a list
*	Trying to slice them or add them – you can't
*	Using square brackets instead of curly brackets when defining them
*	Using curly brackets to index them
*	Expecting things to work with values when they actually work with keys (e.g. for loops, in, max)
*	Using floating point numbers as keys. This is a bad idea, though Python won't stop you trying it. Remember the problem with slight inaccuracies in floats? Using floats as keys involves checking floats for equality – which you should always avoid. You might get away with it – or you might not.
