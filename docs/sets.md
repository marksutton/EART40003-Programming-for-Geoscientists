# Sets

Sets are yet another type of container class (= iterables, collections). See the [Set definition](definitions.md#set). Sets are pretty straightforward – they are equivalent to sets in maths. They can contain only one of any given element value. They don't have any equivalent to indices or keys, but you can iterate over them using for – sets are unordered\*, so don't expect iteration to give you the elements in any particular sequence. Set elements can be strings, numbers, and various other types, but not every Python object can be a set element. In particular, lists, sets and dictionaries cannot be elements of a set. Sets are one of those things that you won't use all that often (unlike lists and dictionaries, which you will use all the time) – but just occasionally they are precisely what is required.

\*The order of set elements is not defined.

You define sets using curly brackets – Python knows this is a set definition not a dictionary definition, as there are no colons.

Sets can only contain one of any given value – if you try to add the same value again, it has no effect. So

```python
a_set = {1, 3, 2, 1}
print(a_set)   # prints {1, 2, 3} on my system
```

Notice that the second '1' vanished, and that the order of the numbers in the set was not maintained. I say 'on my system' as the ordering of unordered collections is 'not defined' – you should make no assumption, and it might be different in different versions of Python and on different computers.

You can't use + to add sets – use the update method instead. You can't slice or index sets. You CAN subtract sets though, which gives the difference between the sets

Use the *in* condition to check if something is in a set.

```python
print(2 in a_set)   # prints True
```

See [Set methods](#set-methods) for a list of useful Set methods. For instance, to add an item to a set, use add:

```python
a_set.add(4)        # set is now {1, 2, 3, 4}
```

You can make a set from a list with

```python
a_set = set(a_list)
```

And a list from a set with

```python
a_list = list(a_set)
```

And finally – there is no curly-bracket syntax to make an empty set, but you can use

```python
empty_set = set()
```

## Set methods

These are methods not functions, so the syntax uses the ‘.’ after an object of type set. For example, use **my_set.clear()** not **clear(my_set)** to clear the set.

Some set methods return a new modified copy of the set, others modify it in place. Read the descriptions!

### `clear()`

**Returns:** N/A

Clears the set, i.e. deletes all items within it

### `copy()`

**Returns:** set

Returns a copy of the set. This is NOT the same as using =. You CAN do set_a = set_b, but that doesn't make a copy – set_a just refers to the same copy of the set as set_b, so if you change set_a, you are also changing set_b. Use copy to make a real copy you can modify separately.

### `add(element)`

**Returns:** N/A

Adds an element to the set in place.

### `remove(element)`

**Returns:** N/A

Removes the element specified from the set, or throws an exception if no such element exists.

### `difference(otherset)`

**Returns:** set

Calculates the difference between sets, i.e. removes if any element of the set is also in *newset*, it is removed. This is the same as using the – operator (so a.difference(b) is the same as a-b).

### `intersection(othersets)`

**Returns:** set

Returns a set containing elements common to this set and all sets in *othersets* (*othersets* can be more than one set, as a list of arguments separated by commas).

### `union(othersets)`

**Returns:** set

Returns the union of the set and all sets in *othersets* (*othersets* can be more than one set, as a list of arguments separated by commas). The union is a set containing all elements that are in ANY of the sets.

### `pop()`

**Returns:** varies

Removes an arbitrary element from the set, and returns it.

[Return to the site index](index.md)
