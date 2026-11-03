# Importing modules

The import keyword is used to import items (functions, classes, constants) from external modules into your program, so you can use them. A single import statement works for the entire .py file. It’s normal to put all required imports right at the start of your files.

To provide flexibility (or to add confusion?) you can use import in several different ways. The simplest is:

<div class="syntax-template" style="font-family:inherit; background:#f4f7fa; border-left:3px solid #5483bc; padding:0.5em 0.8em; margin:0.8em 0">
<p style="margin:0">import module [as alias] # the ‘as alias’ is optional</p>
</div>


For instance:

```python
import math
import numpy as np
```

Once this is done, you can use anything from the imported module, but you must prefix it with *modulename.* (module name is the name of the module, or the alias if you gave one). So

```python
math.sin(angle)   # use the sin function from math module
np.var(my_data)   # use the var function from numpy module
```

If the need to prefix with *modulename.* annoys you, there is an alternative! You can use:

```python
from module import items
```

Where *module* is a module (like math), and *items* is a comma-separated series of items you want to import. Once this is done, you can use the items WITHOUT the modulename prefix. e.g...

```python
from math import sin, cos, pi
```

… lets you use the sin and cos functions, and the pi constant, without needing to prefix them.

Finally, you CAN also import all items from a module like this, using \*

```python
from math import *
```

`from module import *` is legal Python and you will see it in other people's code, but it is normally best avoided. Importing the module itself, or explicitly importing the particular names you need, makes it much clearer where functions and constants came from and avoids accidental name clashes.

## Custom modules (multi-file projects)

So far, we’ve always written a Python program in a single file. That’s fine when programs are short, but as they get longer you’ll find that it becomes inconvenient – you’ll need to do a lot of scrolling up and down to find code, and it gets unwieldy. You may also find that you have certain functions that you want to make available to more than one program. While you *can* just copy/paste them in whenever you need them, if you make any changes you then have to do that in more than one place

Python makes it easy to create your own modules, and to use this concept to split your code over multiple files (and to use certain modules in more than one program if you want to).

To create a module, all you need to do is to create a python file that defines the functions you want in your module, and make sure it’s in the same folder as your ‘main’ program file. You then import it using the filename (without the .py), in exactly the same way as you would import modules like *math*. So, for example, you might create a file called ‘*squarefunctions.py*’ that looks like:

```python
def square_add_one(value):
    return value**2 + 1
```

```python
def square_minus_one(value):
    return value**2 - 1
```

You could then use your new *squarefunctions* module in a different python file like this:

```python
import squarefunctions as sqf
```

```python
print(sqf.square_add_one(10))
print(sqf.square_minus_one(10))
```

## Looking up library functions

I'm not providing any reference materials here – we will be using functions from both the *math* and *random* libraries, but it's time for you to start getting into the habit of looking up what's available and how they work online!

[Return to the site index](index.md)
