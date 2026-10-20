# Lists

The Python list class is a [container class](definitions.md#container); list objects hold a number of *elements*, each of which can be any Python object. Lists can hence hold numbers (e.g. 1,3,7 etc), strings ("this","is","a","list"), or combinations of these or any other type (e.g. 4.7, 4, True, "text"). Lists are ordered, and elements are referred to with an *index*, i.e. their position in the list (starting at 0 not 1). So in the list of four string elements "one", "two", "three", "four", the index of the element "three" is 2 (it's the third element, but we start counting at 0 not at 1, so indices are 0, 1, 2 and 3). Lists can be any length, including length 0 – we refer to a list of length 0 as an empty list.

Python uses square brackets to indicate a list, and elements are separated by commas, so lists in your code will look like [1, 2, 10, 20].

## Creating lists

```python
my_list = [1, 20, 7]    # Make a list with the elements 1, 20, and 7, in that order
empty_list = []      # Make an empty list (with no elements, ready to have some added later)
```

You can also make an empty list with

```python
empty_list = list()      # Make an empty list (with no elements, ready to have some added later)
```

Think of this use of *list* as if it were a built-in function that makes a list\*. If you give it no argument (as above) it gives you an empty list, but if you give it 'something list-like' as an argument, it will turn it into an actual list. By 'something list-like' (and I'm being deliberately vague here), in practice I mean either the return result of the [range function](functions.md#rangestart-stop-step), or a 'tuple' – we'll cover tuples later in the course. So…

```python
one_to_ten_list = list(range(1,11))  # Make a list [1, 2… 9, 10]
```

> **Technical note — optional:** Feel free to ignore this if you don't feel technically minded!
>
> Actually, what seems to be a list function isn't really a function – it’s a 'constructor' method. All objects (which is everything in Python) have a constructor – a special method that is called when they are created – you call it by using brackets after the class name, hence list(). You can also do things like str() and int() to make empty ints, strings etc. We haven't been doing that because the fundamental Python types like int and str also let you assign values with the more convenient and more readable '=' operator, but a lot of custom classes you may come across don't, so you'll have to create them using the constructor. Most constructors take optional arguments, to set the object up according to some rules. The list constructor knows about things like immutable sequence types and tuples, so you can pass these to it and it will make a list from them – that's what's happening when you do list(range(10)).

## Slicing and indexing

List slicing and indexing uses *the same* syntax as string slicing – see [String slicing syntax](strings.md#string-slicing-syntax). You use indices in the same way as well (e.g. `my_list[4]` is the 5<sup>th</sup> item, `mylist[-1]` is the last item).

### Method, functions, operators

You can join lists using the + operator, so

```python
print([1, 2, 4] + [5, 8, 10])  # Prints [1, 2, 4, 5, 8, 10]
```

There are several built-in Python functions that work with lists – see [Functions](functions.md) for some of the more useful ones. For instance *len* (which works on strings to give the string length) also works on lists, to give the number of elements, so…

```python
print(len(["one", "ten", "fifty"]))  # Prints 3 (the length of the list)
```

There are also several useful methods of the list class – see [List methods](#list-methods) below. Remember that methods use the 'object.' notation, so to use the *reverse* method…

```python
reverse_list = ["one", "ten", "fifty"]	# Set reverse_list to ["one", "ten", "fifty"]
reverse_list.reverse()                 # Reverse it – it will now be ["fifty", "ten", "one"]
```

If at this point you find yourself asking "Why are some things functions and others methods, what's the logic in what goes where, and why do there have to be two separate systems"… you are not alone! There isn't any hard-and-fast logic in this, although as a rule of thumb most of the functions (len, min, max etc) work on many different types of containers (and strings), not just lists, while the methods are more list-specific. Not all though, and there are *some* tasks (like sorting) for which both a method and function exist – this can add to the confusion. I'm afraid this is just something you have to get used to – Python is not unique in having this sort of 'two different approaches used at different times' kind of feel to it – this is true of many languages, and reflects their historical 'accretion' as much as anything else. In the end, if you can't remember which way it's meant to be, just Google it, and don't lose sleep over trying to work out *why* things have to be done in particular ways!

List comprehensions are another part of list syntax – these are described on a [separate page](list-comprehensions.md), as you'll need to understand *for* loops before thinking about them.

### Common errors

- Forgetting the square brackets

- Getting the start index wrong – it's 0 not 1!

- Confusing index with element. For instance, the *remove* method takes an element, the pop method takes an index.

- Confusing append and extend. Read the details – they are not the same thing.

- Using methods before creating the list. You can't. If you want to append things onto a list in a loop, you have to make an empty list first.

## List methods

These are methods not functions, so the syntax uses the ‘.’ after an object of type list. For example, use **mylist.sort()** not **sort(mylist)** to sort the elements of a list into order.

Note that unlike string methods, **many of these don't just return a new modified copy of the list** – they modify the original list in-place (and typically don't return anything). See descriptions.

### `append(value)`

**Returns:** N/A

Appends *value* to the end of the list. *Value* can be any valid Python object. Note that if you want to add another list to the end of this list, don't use *append*, which will create a single extra element of type list! Use *extend* instead, or add the lists with the + operator.<br>*append* modifies the list in-place, so doesn't return anything.

### `count(element)`

**Returns:** int

Counts how many times the element *element* occurs in the list, returning an integer. So **[1,2,2,3,4,3,2,4,1,4,1].count(1)** returns 3.

### `extend(newlist)`

**Returns:** N/A

Adds the elements of *newlist* to the end of this list. *Extend* modifies the list in-place, so doesn't return anything.

### `insert(index, element)`

**Returns:** N/A

Inserts a new element into the list at position *index*.

### `pop(index)`

**Returns:** varies

Removes the element at position *index* from the list, and returns it. Note that this is different from *remove*, which needs the value of the element, not the index number (and doesn't return anything).

### `remove(element)`

**Returns:** N/A

Removes *element* from the list – note that this takes an element, not an index number (use *pop* instead if you want to do that). If the element doesn't exist, an exception is thrown.

### `reverse()`

**Returns:** N/A

Reverses the order of the list. Affects the list in-place, so doesn't return anything.

### `sort()`

**Returns:** N/A

Sorts the list in-place, into numerical or alphabetical order. Does not return anything. NOTE – there IS also a sorted function (not a method) that does much the same thing.

[Return to the site index](index.md)
