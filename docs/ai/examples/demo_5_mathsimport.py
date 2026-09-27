# mathsimport.py - common forms of import statement
# and use of some trigonometry functions

import math  # import math library functions are math.funct

# if we added the 'as m' bit ...
# import math as m
# we could use 'm.' instead of math.
# not worth it here... but often used
# for modules with longer names

# THIS import syntax:
# from math import cos, tan, radians
# allows us to use cos and tan (and only those)
# without the 'math.'
# note linter complaining as I don't use tan!

# this next line would import all math functions
# from math import *
# and enable use without 'math.'
# Tempting... but be careful!
# If two modules have functions with
# same name, one is overwritten

angle = 30.0                 # an angle, in degrees
angle = math.radians(angle)  # convert to radians

print(math.sin(angle))       # calculate sine - use math.
# print(cos(angle))  # cosine - no math. - this needs one of last two imports

# Some things in math are not functions!
# pi is a constant - a value you can use
# other modules also define classes
print(math.pi)
