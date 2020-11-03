Conditions are expressions that Python can evaluate to ‘True’ or ‘False’, and are used in a) if / elif / else blocks, and b) while loops.  

i) Boolean value:
-------------------

just a True or False value. Note True and False have an initial capital letter in Python. These aren’t very practical, though occasionally a 
while loop that never ends because of the condition is useful (as you can also exit it with a break statement if you need to).

<pre>
while True:
   Code to keep looping over forever
</pre>

ii) Using a comparison operator. 
-------------------
(e.g. `if a > 10:` ).  Comparison operators available are:  

* \>, <         greater than, less than. Can only use on numbers.  
* \>\=, <\=     greater than or equal to, less than or equal to. Can only use on numbers.  
* \=\=, !\=      equal to, not equal to. Can use on any types (including strings)  

<pre>a > 10</pre>
True is a is more than 10, False if a is 10 or lower  

<pre>b <= 10</pre>
True if b is 10 or less, False if b is higher than 10  

<pre>a == b</pre>
True if the values of a and b are precisely equal, otherwise False. Note two = signs!  

<pre>a != "cat"</pre>
False if the string variable a is "cat", True if it is anything else. Note that string comparisons are case sensitive – if  a holds "Cat" then the condition evaluates to True.  

iii) Compound conditions (boolean operators).
---------------------

Often you want more complex conditions. To construct these, use the and and or ‘Boolean operators’, e.g. if a > 10 and b > 10:

* **and**: both of the conditions need to be True
* **or**: one (or both) of the conditions need to be True

so if a is 5, b is 15
<pre>
a > 10 and b > 10
</pre>
is False (only one of the conditions is True)  
<pre>a > 10 or b > 10</pre>
is True (only one of the conditions is True, that’s enough for ‘or’)  

You can chain these together to make even more complex conditions, but always use brackets to 
make sure you control the order (the most deeply nested brackets are calculated first). It can make a difference.

Consider:
<pre>(a > 10 and b < 10) or b > 13</pre>
This is True. Neither condition in the ‘and’ bit in brackets is True, so that evaluates to False – but b IS greater than 13, so the ‘or’ bit, done last, is True, and the overall expression is True  
 
<pre>a > 10 and (b < 10 or b > 13)</pre>
Here the brackets have moved so the ‘or’ gets done first. b is > 13 so the bracket evaluates to True, but a > 10 is False so the final ‘and’ evaluates to False, and the overall expression is False  

Finally (but less commonly useful) there is also a not Boolean operator, which flips True=>False and False=>True. So  
<pre>
not (a > 10)
</pre>
False if a is more than 10, True if a is 10 or lower  
<pre>not (a == b)</pre>
False if the values of a and b are precisely equal, otherwise True. This is precisely equivalent to `a != b`.  

**'in' conditions**

A nice simple feature! You can use the keyword in to find out whether an element is in a list (or in any type of container class). The condition:

`check_element in container`

is True if there is one of more element in container matching the check_element. e.g.

<pre>if "one" in number_list:
    print("'One' found in the list")
</pre>

Common errors to watch out for with conditions:
-------
* Using a single equals sign. Single equals assigns values to variables. Use double equals for comparisons.
* Missing off a variable name in second condition of an and/or. This is a very common ‘rookie’ error, because in English, `a>10 or <0` makes perfect sense. It doesn’t to Python. You need a > 10 or a < 0.
* Misunderstanding order of evaluation of complex conditions – see above – use brackets to control it, don’t assume you know which order things happen in. 
* Mixing types in an illegal way, e.g. `a < 5` is illegal if a is a string
* Trying to do precise (\=\= or !\=) comparisons with floating point (i.e. non-integer) numbers. These don’t always work. This is a counterintuitive and complex issue, which we will cover properly next week. Ignore for now… but keep it at the back of your mind.
