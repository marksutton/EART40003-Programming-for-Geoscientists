# scatterplot.py - plotting scatter data of student marks

import matplotlib.pyplot as plt

infile = open("first_year_marks.csv", "r") 	# open my data file

headerline = infile.readline()  	# read headings - will ignore them
lines = infile.readlines()		# read all other lines into a list of strings
infile.close()

# next - revision! - go through data and get two lists, one for fieldmarks,
# and the other for yearmarks

fieldmarks = []						# set up empty lists for fieldmarks...
yearmarks = []					    # ... and yearmarks

for line in lines:					    # for each line in the data
    data = line.split(',') 				# split line on comma into a list
    fieldmarks.append(float(data[0]))    # store 1st item (the fieldwork mark)
    yearmarks.append(float(data[1]))		# store 2nd item (overall year mark)

# Now do the plot...

plt.plot(fieldmarks, yearmarks, 'r.', markersize=10,
         markeredgewidth=1)
# 'bx' - blue 'x' markers, 10 points in size,
# drawn in a thickish line.

plt.xlim(0, 100)    # both scales 0-100
plt.ylim(0, 100)

# set up ticks - these ARE in odd places, as we want grade boundaries
plt.xticks([0, 40, 50, 60, 70, 100],
           ["0%", "3rd/Fail", "2ii/3rd", "2i/2ii", "2i/1st", "100%"],
           rotation="vertical")
plt.yticks([40, 50, 60, 70, 100],
           ["3rd/Fail", "2ii/3rd", "2i/2ii", "2i/1st", "100%"])
# ticks and labels to set up by category boundaries

plt.grid(linestyle='--', linewidth=1,   # turn on grid with
         color='green')                 # thin dashed green lines
# notice - grid follows the x/y ticks

# labels and titles
plt.ylabel("Overall Year Mark", weight='bold')
plt.xlabel("Mark for Fieldwork", weight='bold')
plt.title("Fieldwork and Year marks 2015-16", weight='bold')


plt.show()		# finally - show the chart
