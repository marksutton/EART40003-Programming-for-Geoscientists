# tuples.py - demo of returning multiple values with a tuple
# also demonstrates the random module.

# This code imports the 'random' module as rnd. Imports should always be at the
# beginning of you python files.
# See: https://docs.python.org/3/library/random.html
import random as rnd


# Returns a pseudo-random number between minimum and maximum
def rand_float_between(minimum, maximum):
    # basic random function - gets random float 0-1
    r = rnd.random()

    # convert to correct range - multiply by range-size
    # same as writing: r = r * (maximum - minimum)
    r *= (maximum - minimum)

    # and add minimum value
    # same as writting: r = r + minimum
    r += minimum

    # done ... return it
    return r


# Function that takes two floats as arguments.
# Returns a tuple of three random floats between these
# values which are in order.
def three_ordered_random_numbers(minimum, maximum):
    # uses rand_float_between custom function (see above)
    # lowest number - anywhere between min and max
    lowval = rand_float_between(minimum, maximum)

    # uses rand_float_between custom function (see above)
    # highest - anywhere between lowest and max
    highval = rand_float_between(lowval, maximum)

    # uses rand_float_between custom function (see above)
    # finally middle value - anywhere between highest and lowest
    midval = rand_float_between(lowval, highval)

    # done ... and return the values as a tuple
    return (lowval, midval, highval)


# Call tuple-generating function and upack into low, mid, high
low, mid, high = three_ordered_random_numbers(0, 1)

# print them
print(f"Values are: {low:.3f}, {mid:.3f}, {high:.3f}")
