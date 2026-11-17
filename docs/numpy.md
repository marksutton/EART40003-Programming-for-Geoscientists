# NumPy arrays

The examples use `import numpy as np`; see [Importing modules](modules.md).

NumPy is all about arrays. NumPy arrays (which I’ll just call arrays from now on) are a container class designed for efficient computation. In some circumstances they can be more than 500 times faster than Python lists, and can normally save you coding time too, because of [vectorization](#vectorization).

Arrays are a bit like lists, except that they (a) have a fixed number of elements (you can’t add or remove them without making a new array), and (b) all elements need to be of the same type (normally *float*, occasionally *int*). You can’t make an array directly using anything like the square bracket notation used for lists, but you can turn a list into an array using the NumPy *array* constructor, so to make an array with values [1 2 3 4] you can use:

```python
small_array = np.array([1, 2, 3, 4])
```

Arrays are designed to easily work with multidimensional data (e.g. two-dimensional data in tables) as well as single-dimensional data (equivalent to a list). Recall that you can model multi-dimensional data using lists by using lists within lists – you can convert these directly to a multidimensional array, so…

```python
two_d_array = np.array([[1, 2, 3],[4, 5, 6]])  # make a 2d array
print(two_d_array)
```

…will convert the nested lists-within-lists to a 2D array, which when printed looks like

```text
[[1 2 3]
 [4 5 6]]
```

Note that unlike nested lists, each row must have the same number of elements (here 3). Arrays can happily use numbers of dimensions beyond two, but we will stick to two for this course. Note that when multi-dimensional arrays are printed, they appear using nested square brackets (like above).

You can also make an array with the very useful *zeros* or *linspace* functions – *zeros* to make an array filled with zeros, *linspace* to make an array with a sequence of evenly spaced floating point numbers. Full function descriptions are under [NumPy functions](functions.md#numpy-functions).

```python
five_zeros = np.zeros(5)              # makes array [0. 0. 0. 0. 0.]
three_x_three_zeros = np.zeros((3,3)) # makes a 3x3 array of zeros – note (( ))
spaced_values = np.linspace(0,3,7)    # makes array [0 0.5 1 1.5 2 2.5 3]
```

Notes: With zeros, you need TWO brackets for multidimensional arrays, as what you are passing is actually a tuple. With linspace, the first two arguments are the start and end of the number sequence you want, and the final one is the number of values. This is a bit different to *range*, which (a) only makes integers, and (b) wants it’s equivalent of the ‘stop’ value to be 1 + (last value you want).

Once you’ve made an array, you can alter its number of dimensions with *reshape* if you need to. The [*shape* of the array](#shape) will tell you the current number of dimensions.

You can use convert arrays to lists using the *list* constructor function, e.g.

```python
a_list = list(np.linspace(0, 2, 5))   # a_list is now [0, 0.5, 1, 1.5, 2]
```

## Indexing and slicing

You can index and slice arrays much like lists, so

```python
an_array[4]      # 5th element (arrays start indexing at 0 just like lists)
an_array[4:10]   # 5th through 10th elements
```

For multidimensional arrays, you can index in the same way as nested lists. For example, using the two_d_array created above:

```python
print(two_d_array[1][2])   # prints 6
```

Or, with a NumPy array, you can put the indices together inside one pair of square brackets, separated by a comma:

```python
print(two_d_array[1, 2])   # also prints 6
```

You can slice in multiple dimensions in the same way. For example:

```python
an_array = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 10, 11, 12]])
print(an_array[1:3, 0:2])
```

Prints:

```text
[[ 5  6]
 [ 9 10]]
```

Finally, and unlike lists, NumPy provides a facility for ‘conditional indexing’. This is rather useful. You can provide conditions as indices, and only the elements that meet those conditions will be selected. Examples:

```python
newarray = arr[arr > 10]  # newarray is made from all elements in arr whose value is > 10
newarray = arr[arr % 3 == 0]  # newarray is made from all elements in arr divisible by 3
newarray = arr[(arr <= 100) & (arr >= 50)]  # newarray is made from all elements in arr with values between 50 and 100
```

This is straightforward and obvious for the first two (simple conditions), but notice that the compound condition doesn’t use the normal python ‘and’, it uses ‘&’ instead. I’m not going to go into why, but yes, if you want to use ‘and’ or ‘or’ in this NumPy conditional-index syntax, you DO need to use symbols instead - use & for ‘and’, and ‘|’ for ‘or’ (that’s the vertical bar symbol – shift and backslash on a UK keyboard – they key next to Z). Note that these aren’t alternatives for ‘normal’ conditions that you would use in an *if* or *while* – always use the words ‘and’ and ‘or’ for those. Finally, as another quirk of the syntax, you do need the brackets round the individual conditions if you use & or |.

Finally, there is a superficially similar but in practice different version of this for setting values. If you put the conditional index syntax on the left of the equals, you can set those elements to some value, so

```python
arr[arr > 10] = 10  # set all elements greater than 10 to 10
```

## Vectorization

This is where the real power (and the main point) of arrays lies. Vectorization is writing code that operates on all elements of arrays, in one go. For instance, suppose myarray starts as [1 2 3 4]:

```python
myarray = myarray + 4  # myarray is now [5 6 7 8]
```

You can also write this more compactly as:

```python
myarray += 4
```

which does the same thing.

You can multiply every value in an array in the same way. Starting again with myarray as [1 2 3 4]:

```python
newarray = myarray * 10  # newarray is [10 20 30 40]
```

Starting again with myarray as [1 2 3 4], you can also do calculations using two arrays of the same size:

```python
second_array = np.array([5, 6, 7, 8])
newarray = myarray + second_array  # newarray is [6 8 10 12]
newarray = myarray * second_array  # newarray is [5 12 21 32]
```

This not only saves a lot of code-writing (if you did this with lists you would need to use loops or comprehensions), but it also runs a lot faster. The speed won’t matter if your arrays are only a few hundred elements in size, **but really WILL matter if they contain millions of numbers**.

You can use functions in vectorization – if the function is compatible with it. All the mathematical functions that *NumPy* provides work with it, but some others (e.g. the ones in the *math* module) won’t. So:

```python
angles = np.linspace(0,math.pi,1000)  # array of lots of values 0-Pi
sines =  np.sin(angles)    # vectorizes fine – this is the NumPy sin function
sines =  math.sin(angles)  # Will throw an error – math.sin expects a number
```

Writing your own functions that work with vectorization is easier than you think – for most simple functions that do some calculation on their argument, it will just work without you realising why. We’ll show an example of this in class.

## Array methods and attributes

These are methods not functions, so the syntax uses the ‘.’ after an object of type array. For example, use **myarray.reshape(10,10)** not **reshape(myarray,10,10)** to reshape to a 10 x 10 array.

### `copy()`

**Returns:** array

Returns a copy of the array. As with all objects in Python except fundamental types like int and float, this is NOT the same as using =. *newarray* = *oldarray* will appear to work, but you aren’t making a copy – both *newarray* and *oldarray* refer to the same array in memory, so if you change one, you are changing both. To make a genuine new copy that you can modify separately, you need to use copy, e.g.  *newarray* = *oldarray.copy()*

### `reshape(size)`

**Returns:** array

Returns the array reorganised into the specified number of rows and columns (size is the same as in the *zeros* function – it can be either a single integer, or a tuple for multidimensional arrays. The original array must have the same number of elements as the reshaped one. So if myarray is [1 2 3 4 5 6], myarray.reshape((2,3)) turns it into<br>[1 2 3<br>4 5 6]<br>Note that unlike zeros, this WILL work without the second set of brackets, as reshape allows dimensions to be specified with normal arguments rather than a tuple (but also does understand tuples). It’s best to use the extra brackets anyway though, as in the end you’ll forget which functions need them and which don’t!

### `shape`

**Type:** tuple of ints

shape is not actually a function or method - it is a value attached to the array which tells you the size of each dimension. This means you don't put () after it as you would with a function or method. So if your array (called myarray) is a 5 x 6 array (5 rows, 6 columns), printing myarray.shape gives you (5, 6). Printing myarray.shape[1] gives you 6 (because the first dimension is rows, the second is columns).

> **More:** There are rather a lot of methods for array – see e.g. <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html> Look them up if you need them – or if you aren’t sure if the thing you want to do might have a method, browse the list and find out!

[Return to the site index](index.md)
