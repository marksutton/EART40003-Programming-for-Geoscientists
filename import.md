Importing modules
=================

The import keyword is used to import items (functions, classes, constants) from external 
modules into your program, so you can use them. A single import statement works for the 
entire .py file. It’s normal to put all required imports right at the start of your files.

To provide flexibility (or to add confusion?) you can use import in several different ways. 
The simplest is:

<pre>import module [as alias]     # the 'as alias' is optional
</pre>
For instance:

<pre>import math
import numpy as np
</pre>

Once this is done, you can use anything from the imported module, but you have to prefix it with 
modulename. (module name is the name of the module, or the alias if you gave one). So

<pre>
math.sin(angle)   # use the sin function from math module
np.var(my_data)   # use the var function from numpy module
</pre>

If the need to prefix with modulename. annoys you, there is an alternative! You can use:

<pre>from module import items
</pre>

Where _module_ is a module (like math), and _items_ is a comma-separated series 
of particular items you want to import. Once this is done, you can use the items 
WITHOUT the modulename prefix. e.g.

<pre>from math import sin, cos, pi
</pre>

Lets you use the sin and cos functions, and the pi constant, without needing to prefix them.

You CAN also import all items from a module like this, using *

<pre>from math import *
 </pre>
 
This brings in all items from the math module – you can now use them without the prefix. 
At first sight this will look like the easiest and best way forward – it certainly cuts down 
on typing – but there is a catch. If you do an import * from several modules, and two of 
them use the same function name (e.g. both have a count function, but these do different things) 
then you have a recipe for confusion and bugs. For this reason, it’s best to use the other forms of 
import, so you can be sure you won’t run into this sort of name-clash. That said, if you are only 
importing ONE module then you will be fine with the * form. Feel free to use it when appropriate – 
it’s certainly fine if you only import one module - but programs that start with seven 
import * lines are likely to be marked down for bad style.
