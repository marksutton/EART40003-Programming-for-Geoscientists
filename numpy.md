Numpy is all about arrays. Numpy arrays (which I’ll just call arrays from now on) are a container class designed for efficient computation. 
In some circumstances they can be more than 500 times faster than Python lists, and can normally save you coding time too, because of vectorization (see later on).

Arrays are a bit like lists, except that they (a) have a fixed number of elements (you can’t add or remove them without making a new array), and 
(b) all elements need to be of the same type (normally float, occasionally int). 
You can’t make an array directly using anything like the square bracket notation used for lists, but you can turn a list into an array 
using the numpy array constructor, so to make an array with values [1 2 3 4] you can use:

<pre>
small_array = np.array([1, 2, 3, 4])
</pre>

Arrays are designed to easily work with multidimensional data (e.g. two-dimensional data in tables) 
as well as single-dimensional data (equivalent to a list). Recall that you can model multi-dimensional data 
using lists by using lists within lists – you can convert these directly to a multidimensional array, so…

<pre>
two_d_array = np.array([[1, 2, 3],[4, 5, 6]])  # make a 2d array
print(two_d_array)
</pre>

…will convert the nested lists-within-lists to a 2D array, which when printed looks like
<pre>
[[1 2 3]
 [4 5 6]]
</pre>

Note that unlike nested lists, each row has to have the same number of elements (here 3). 
Arrays can happily use numbers of dimensions beyond two, 
but we will stick to two for this course. Note that when multi-dimensional arrays are printed, they appear using nested square brackets (like above).

You can also make an array with the very useful `zeros` or `linspace` functions – `zeros` to make an array filled with zeros, 
`linspace` to make an array with a sequence of evenly spaced floating point numbers. See numpy functions section.

<pre>
five_zeros = np.zeros(5)              # makes array [0 0 0 0 0]
three_x_three_zeros = np.zeros((3,3)) # makes a 3x3 array of zeros – note (( ))
spaced_values = np.linspace(0,3,7)    # makes array [0 0.5 1 1.5 2 2.5 3]
</pre>

Notes: With `zeros`, you need TWO brackets for multidimensional arrays, as what you are passing is actually a tuple. 
With `linspace`, the first two arguments are the start and end of the number sequence you want, and the final one is the number of values.
This is a bit different to range, which (a) only makes integers, and (b) wants it’s equivalent of the ‘stop’ value to be 1 + (last value you want).

Once you’ve made an array, you can alter its number of dimensions with reshape if you need to. 
The `shape` ‘constant’ of the array (see above) will tell you the current number of dimensions.

You can use convert arrays to lists using the list constructor, e.g. 

<pre>a_list = list(np.linspace(0, 2, 5))   # a_list is now [0, 0.5, 1, 1.5, 2]
</pre>

Indexing and slicing
--------------------
You can index and slice arrays much like lists, so

<pre>an_array[4] # 5th element (arrays start indexing at 0 just like lists)
an_array[4:10] # 5th through 11th elements
</pre>

For multidimensional arrays, you can index in the same way as lists…

<pre>print(two_dimensional_list[2][1])
</pre>
… or you can use the indices separated with commas inside the square brackets (which is the same way most other languages do it):

<pre>
print(a_list[2,1])
</pre>

And you can slice in multiple dimensions as well. For example:

<pre>
an_array = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]) # make 2d array
print(an_array[1:3,0:2])
</pre>

Prints:

<pre>[[ 5  6]
 [ 9 10]]
</pre>

Finally, and unlike lists, numpy provides a facility for ‘conditional indexing’. This is rather useful. 
You can provide conditions as indices, and only the elements that meet those conditions will be selected. Examples:
 
<pre>
newarray = arr[ar > 10]  # newarray is made from all elements in arr whose value is > 10
newarray = arr[ar % 3 == 0]  # newarray is made from all elements in arr divisible by 3
newarray = arr[(ar<=100) & (ar>=50)]  # newarray is made from all elements in arr beween 0 and 50
</pre>

This is straightforward and obvious for the first two (simple conditions), but notice that the compound condition doesn’t use the normal python ‘and’,
it uses ‘&’ instead. I’m not going to go into why, but yes, if you want to use ‘and’ or ‘or’ in these numpy conditional index syntax, you 
DO need to use symbols instead - use & for ‘and’, and ‘|’ for ‘or’ (that’s the vertical bar symbol – shift and backslash on a UK keyboard – they key next to Z). 
Note that these aren’t alternatives for ‘normal’ conditions – always use the words ‘and’ and ‘or’ for those. Finally, as 
another quirk of the syntax, you do need the brackets round the individual conditions if you use & or |.

Finally, if you put the conditional index syntax on the left of the equals, you can set those elements to some value, so

<pre>arr[ar > 10] = 10  # set all elements greater than 10 to 10  
</pre>

Vectorization
--------------

This is where the real power of (and point of) arrays lies. 
Vectorization is writing code that operates on all elements of arrays, in one go. For instance, you can use: (for the following examples, `myarray` starts as `[1 2 3 4]`)

<pre>
myarray = myarray + 4  # myarray is now [5 6 7 8]
myarray += 4           # even more efficient version of the above

newarray = myarray * 10  # newarray is [10 20 30 40]

second_array = np.array([5, 6, 7, 8])
newarray = newarray + second_array  # newarray is [6 8 10 12]
newarray = newarray * second_array  # newarray is [5 12 21 32]
</pre>

This not only saves a lot of code-writing (if you did this with lists you would need to use loops or comprehensions), it also runs a lot faster. 
This won’t matter if your arrays are only a few hundred elements in size, but really WILL matter if they contain millions of numbers.

You can use functions in vectorization – if the function is compatible with it. All the mathematical functions that numpy provides work with 
it, but some others (e.g. the ones in the math module) won’t. So:

<pre>
angles = np.linspace(0,math.pi,1000)  # array of lots of values 0-Pi
sines =  np.sin(angles)    # vectorizes fine – this is the numpy sin function
sines =  math.sin(angles)  # Will throw an error – math.sin expects a number
</pre>

Writing your own functions that work with vectorization is easier than you think – for most simple functions that do some calculation on their argument, 
it will just work without you realising why. We’ll show an example of this in class.
