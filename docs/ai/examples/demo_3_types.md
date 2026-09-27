---
---
{% raw %}
# demo_3_types.py

Return to [Demonstration programs](index.md).

````python
# types.py - demonstrate the fundamental python types - int, float, str, bool

a = 10
print(type(a))      # a is an int

a = a + 1
print(type(a))      # a is still an int

a = a / 2
print(type(a))      # a is now a float

b = 5.23            # set up b as a float

if type(b) == float:
    print("b is a float")       # prints (as b is a float)
else:
    print("b is NOT a float")   # doesn't print

b = b - 0.23        # b is now 5.0 - but is still a float!

if type(b) == float:
    print("b is still a float")   # this prints...
else:
    print("b is NOT a float")     # this doesn't

s = "some text"              # set up s as a string
print(type(s))               # print its type (str)

a_boolean = True             # set up a_boolean as a bool
print(type(a_boolean))       # print its type (bool)

another_boolean = a < 0      # set up another_boolean (will be False)
print(another_boolean)       # print it to check

if another_boolean:          # can use it in conditions...
    print("a was less than 0")
else:
    print("a was NOT less than 0")
````
{% endraw %}
