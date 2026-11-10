# Dictionaries

Dictionaries are another type of container class (= iterables, collections). See the [Dictionary definition](definitions.md#dictionary). A good way to think about them is as look-up tables. Dictionaries don't have indices like lists – instead they have 'keys', which are much more flexible. Dictionaries can be set up in code like lists, except that they use curly brackets { } instead of square brackets [ ]. For example:

```python
digit_dict = {"one":1, "two":2, "three":3, "four":4, "five":5,
      "six":6, "seven":7, "eight":8, "nine":9}
```

Notice that each item has two pieces of data – the first (before the colon) is the key, and the second is the value, or element. Notice also that I split the line – you are allowed to do this without a \ inside curly brackets (or any brackets for that matter). Keys are used like indices to look up elements, so

```python
print(digit_dict["two"])   # prints 2
```

Perhaps slightly confusingly, Python still uses square brackets to look things up in dictionaries, just like indexing in arrays. It might have made more sense if they used curly brackets, but they didn't. Curly brackets are only used for defining 'pre-made' dictionaries in code.

For the purposes of this course, dictionary keys should be strings or numbers. Python does allow some other types of object to be used as keys, but there are restrictions on which ones are allowed, and we don't need to worry about those here. Elements can of course also be any type – that includes other collections like lists and dictionaries. You are allowed to have different element types in one dictionary, but (once more) it's probably not a good idea. 99% of the time you'll want to use dictionaries where all the keys are of one type, either numbers or strings, and all the elements are of one type as well (which could be just about anything).

Keys must be unique – you can't have two keys the same. If you set the value for a key twice, the second value replaces the first. This is one way in which keys work exactly like list indices.

You can iterate over dictionaries using *for* loops, but what you are iterating over is the keys, not the values. This isn't a problem, unless you expect it to be the values! So…

```python
for i in digit_dict:
    print(i)
```

prints "one", "two" … "nine" (the keys). If you want to print the values, just look them up in the dictionary – so use

```python
for i in digit_dict:
    print(digit_dict[i])
```

which prints 1,2…9

## Using dictionary methods

See [Dictionary methods](#dictionary-methods) for a list of useful methods. The most important is probably *update*, which adds an entire new dictionary to the first. The following line adds two new key/value pairs:

```python
digit_dict.update({"ten":10, "eleven":11})
```

To add a *single* item (i.e. a single key/value pair), you can instead just use  dictionary_name[key] = value, e.g.

```python
digit_dict["twelve"] = 12
```

To remove items use the *pop(key)* method*.* To get a list-like object containing the values, use the *values()* method, and to get a list-like object containing the keys, use the *keys()* method.

Note – there ARE such things as dictionary comprehensions. If you feel brave, look ‘em up! I won’t be teaching them in this course.

## Differences between dictionaries and lists

Dictionaries preserve insertion order: if you iterate with *for*, the key/value pairs will be encountered in the order in which you added them. However, dictionaries are accessed by keys rather than numerical positions, so there is no slicing syntax.

Some of the Python functions that work on lists also work on dictionaries. *len* does what you expect (gives you the number of key/value pairs). *max, min* and *sum* also work, but they work on the keys not the values, which is probably **not** what you expect.

You can use *in* in a condition just like in a list – but (again) it's the keys not the values that are searched.

You can't add dictionaries with +. Use the *update* method instead

## Common errors

- Not being aware of whether a particular object in your code is a dictionary or a list

- Trying to slice them or add them – you can't

- Using square brackets instead of curly brackets when defining them

- Using curly brackets to index them

- Expecting things to work with values when they actually work with keys (e.g. *for* loops, *in*, *max*). If you want to loop over values not keys, use something like **for v in my_dict.values():**

- Using floating point numbers as keys. This is a bad idea, though Python won't stop you trying it. Remember the problem with slight inaccuracies in floats? Using floats as keys involves checking floats for equality – which you should always avoid. You might get away with it – or you might not.

## Dictionary methods

These are methods not functions, so the syntax uses the ‘.’ after an object of type dictionary. For example, use **mydict.values()** not **values(mydict)** to get a list-like object containing the values.

Like list methods, (and unlike string methods), many of these don't just return a new modified copy of the dict – they modify the original dictionary in-place (and typically don't return anything). See descriptions.

### `clear()`

**Returns:** N/A

Clears the dictionary, i.e. deletes all items within it

### `copy()`

**Returns:** dict

Returns a copy of the dictionary. This is NOT the same as using =. You CAN do dict_a = dict_b, but that doesn't make a copy – dict_a just refers to the same copy of the dictionary as dict_b, so if you change dict_a, you are also changing dict_b. Use copy to make a real copy you can modify separately.

### `keys()`

**Returns:** list-like object*

Returns a list-like object containing the keys.

### `pop(key)`

**Returns:** varies

Removes the value (element) with the given key, and returns it.

### `update (newdict)`

**Returns:** N/A

Adds all the key/value pairs from *newdict* to the dictionary. This affects the dictionary 'in-place', and doesn't return anything.

### `values()`

**Returns:** list-like object*

Returns a list-like object containing the values.

> **Technical note — optional:** These return values behave a bit like the object returned by `range()` - they are a lot like lists, and you can loop over them with `for`, but technically they aren't lists. I know, I know, Python being obtuse again. If you actually need a list, you can use `list(mydict.keys())` or `list(mydict.values())`.

[Return to the site index](index.md)
