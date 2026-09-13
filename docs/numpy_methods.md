numpy arrays (provided by the numpy module)
=======================

These are methods not functions, so the syntax uses the ‘.’ after an object of type list. For example, use `myarray.copy()` not `copy(myarray)` to make a copy.

Numpy methods tend to return a new modified copy of the array, rather than modify it in place.

**copy() return type: array**
<br />Returns a copy of the array. As with all objects in Python except fundamental types like int and float, this is NOT the same as using =. `newarray = oldarray`
will appear to work, but you aren’t making a copy – both newarray and oldarray refer to the same array in memory, so if you change one, you are changing both. 
To make a genuine new copy that you can modify separately, you need to use copy, e.g.  `newarray = oldarray.copy()`

**reshape(size) return type: array**
<br />Re-organises the array into the specified number of rows and columns (size is the same as in the zeros function – 
it can be either a single integer, or a tuple for multidimensional arrays. The original array must have the same number of elements as the reshaped one.
So if `myarray` is `[1 2 3 4 5 6]`, `myarray.reshape((2,3))` turns it into 
<pre>[1 2 3
 4 5 6]
 </pre>
Note that unlike `zeros`, this WILL work without the second set of brackets, as reshape allows dimensions to be specified with normal arguments rather than a tuple
(but also does understand tuples). It’s best to use the extra brackets anyway though, as in the end you’ll forget which functions need them and which don’t!

**shape type: tuple of ints**
<br />shape is not actually function, it is a ‘constant’ – a tuple with the sizes of each dimension of the array. So if your array (called `myarray`) is a 5 x 6 array 
(5 rows, 6 columns), printing myarray.shape gives you `(5, 6)`. Printing `myarray.shape[1]` gives you 6 (because the first dimension is rows, the second is columns).

**[More!]**
<br />There are rather a lot of methods for array – see e.g. (https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.ndarray.html)[https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.ndarray.html].
Look them up if you need them – or if you aren’t sure if the thing you want to do might have a method, browse the list and find out!
