---
---
{% raw %}
# demo_1_variables.py

Return to [Demonstration programs](index.md).

````python
# demo_1_variables.py - demonstrate basic use of variables
# These # lines are 'comments' - no effect on program

a = 10       # a is a variable, set to the value 10
b = 20       # b is another variable, set to the value 20

print(a)     # print value of variable a (note no quotes!)
print("a")   # to show what happens if you DO put quotes
print(b)     # print value of b
print(a*b)   # work out value of a times value of b, print
print(b-a)   # work out b-a

c = (a+b)*3  # calculation involving a and b - put in variable c

print(c)     # print out value in variable c


# NOTE - I'm using a,b,c for variable names as these are abstract
# examples. In your code, real variable names should be longer to make
# it clear what they represent. e.g. speed, planet_mass, etc.
````
{% endraw %}
