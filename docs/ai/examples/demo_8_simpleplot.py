# simpleplot.py - plotting a function

import matplotlib.pyplot as plt
import numpy as np


def polynomial_3(a, b, c, d, x):
    # return value of 3rd order polynomial
    # a.x^3 + b.x^2 + c.x + d
    return a * x ** 3 + b * x ** 2 + c * x + d


x_values = np.linspace(0, 100, 500)  # lots of x values, 0-100

# work out y values for a particular polynomial - vectorization!
y_values = polynomial_3(-.23, 16.9, -4.2, -1, x_values)

# Now do the plot - by default this gives me no markers, blue lines
# which is fine for what I want here
plt.plot(x_values, y_values)

# labels and titles
plt.ylabel("f(x)", weight='bold')
plt.xlabel("x", weight='bold')
plt.title("Plot of 3rd-order polynomial function", weight='bold')

plt.show()		# finally - show the chart
