Sets
==========

Sets are yet another type of container class (= iterables, collections). 
Sets are pretty straightforward – they are equivalent to sets in maths. They can contain only one of any given element value. 
They don't have any equivalent to indices or keys, but you can iterate over them using for – like dictionaries they are unordered, 
so don't expect iteration to give you the elements in any particular sequence. As usual, set elements can be any type. 
Sets are one of those things that you won't use all that often (unlike lists and dictionaries, which you will use all the time) 
– but just occasionally they are precisely what is required.

You define sets using curly brackets – Python knows this is a set definition not a dictionary definition, as there are no colons.

Sets can only contain one of any given value – if you try to add the same value again, it has no effect. So

<pre>a_set = {1, 3, 2, 1}
print(a_set)   # prints {1, 2, 3} on my system
</pre>

Notice that the second '1' vanished, and that the order of the numbers in the set was not maintained. 
I say 'on my system' as the ordering of unordered collections is 'not defined' – you should make no assumption, 
and it might be different in different versions of Python and on different computers.

You can't use + to add sets – use the update method instead. You can't slice or index sets. You CAN subtract sets though, which gives the difference between the sets

Use the `in` condition to check if something is in a set.

<pre>print(2 in a_set)   # prints True
</pre>

See the [set methods](set_methods.md) document for methods. For instance, to add an item to a set, use add:

<pre>a_set.add(4)        # set is now {1, 2, 3, 4}
</pre>

You can make a set from a list with

<pre>a_set = set(a_list)
</pre>

And a list from a set with

<pre>a_list = list(set)
</pre>

And finally – there is no curly-bracket syntax to make an empty set, but you can use

<pre>empty_set = set()
</pre>
