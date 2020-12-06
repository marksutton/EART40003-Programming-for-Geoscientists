Matplotlib Functions
=========================

You will need to import this module to use them – the conventional alias is plt, so `import matplotlib.pyplot as plt`. 
If you use this, prefix all function calls with ‘plt.’. Another note - a few of these 
functions DO actually return something, but you will rarely use their return values – 
you’ll have them as statements on their own, to create/modify/show the current graph. For this reason I don’t give any details of return values.


**Graph Generation Functions** – use one of these FIRST to set up your graph
--------------------

**bar(left, height, width, bottom, kwargs)**
<br />**hbar(left, height, width, bottom, kwargs)**
<br />bar plots a barchart – well a column chart really – vertical bars. hbar is the horizontal bar equivalent – 
it works in exactly the same way. If you want to label the bars with text (and you probably do), use the `xticks` function.
<br />`left` is a list of values for the left of bars, i.e. their positions. Often you’ll just want whole numbers, so `[1, 2, … 10]` etc.
<br />`height` is a list of height values for the bars – i.e. the actual data.
<br />`width` is either a single value for width of bars or a list of values if there aren’t constant. Same units as left.
<br />`bottom` is either a single value for position of bottom of bars, or a list of values (should you want different bottoms for different bars). 
If omitted (i.e. you just give left, height, width) the default bottom value is 0.
<br />Some kwargs:
* `color`: single colour (or list of colours if you want different colours for each bar). e.g `color=”red”`
* `edgecolor`: single colour or list of colours for lines around the bars. e.g. `edgecolor=”blue”`
* `linewidth`: the width of the lines (0 means no lines) – this can also be a list of values. e.g. `linewidth=2``
* `align =”center”` – if this is specified the values in `left` are middle of bar not left of bar

**hist (data, kwargs)**
<br />Plots a histogram for data. If you can’t remember or don’t know the difference between a histogram and a bar chart, google it!
<br />Some kwargs:
*	`bins`: either a number of bins to use, or a list of bin ‘edge’ values. E.g. `bins = [10, 20, 30, 40, 50]` will result in 4 (not 5) bins, 10-20, 20-30, 30-40, 40-50. 
Values on an edge go into the upper bin (i.e. 20 goes in 20-30 not 10-20).
*	`normed`: set to `True` to make a a normalised histogram (a probability distribution, with an integral of 1)
*	`color`: as for bar function above
*	`edgecolor`: as for bar function above
*	`linewidth`: as for bar function above

**pie(data, kwargs)**
<br />Unsurprisingly – this plots a pie chart. data is a list (or array) or numbers. 
If they sum to more than one, then the size of each slice is just it’s proportional value. 
If they sum to less than one though, they are treated like percentages, and you’ll have a blank slice representing the rest of the data – 
so calling pie on `[.1, .2, .2, .2]` will leave a hole 30% of the pie in size without a slice.  
<br />Some kwargs:
* `explode`: a list or array the same length as data specifying the fraction of the radius with which to offset each wedge.
* `labels`: a list of strings providing the labels for each wedge
* `colors`: a list of colours for the pie slices
* `labeldistance`: the radial distance at which the pie labels are drawn. If set to “None”, labels are not drawn, but are stored for use in a legend.
* `rotatelabels`: set to True to rotate each label to the angle of the corresponding slice.
* `autopct`: format string to include %age values on the chart. e.g. `autopct=”%.1f%%”` for 1 d.p. percentages.

**plot(xdata,ydata,format, kwargs)**
<br />Plots a scatter plot of xdata against ydata, optionally with points joined in sequence by lines. 
This is the most commonly used graph generation function. If you want a scatter plot with errorbars, 
use `errorbar` function instead of plot. There is also a `scatter` function which is very similar to plot.
<br />`xdata` and `ydata` must be lists (or numpy arrays) of numbers, both of the same length. 
<br />`format` is optional (you can use kwargs instead) but is a quick way to specify colour, marker and line style as a short string.
Use the first letter for colour (e.g. `r` for red), a character (e.g. `o` or `*`) for a marker, and then specify a line style, e.g. `-` for solid line, `--` 
for dashed. Leaving out the line style gives you no lines – which is quite often what you want. For example, `“ro”` gives you red circles, no lines. 
If you don’t specify a format and you don’t use kwargs to alter markers/lines either, you get no markers and blue lines joining the points.
<br />Some kwargs:
*	`markersize`: size of marker (in points) e.g `markersize=14`
*	`markerfacecolor`, `markeredgecolor`: colours of fill and outline (respectively) for markers.
*	`markeredgewidth`: outline width for marker in points, e.g. `markedgewidth=0`
*	`marker`: symbol for marker (see online documentation) – or `“None”` for ‘no markers’. 
*	`linewidth`: width of line in points
*	`linestyle`: style of line, e.g. `“-“` (solid), `“--“` (dashed), `“-.”` (dash-dotted), `“None”` (no line).
*	`color`: colour of the line
*	`label`: text to use in the legend for this data series. 
Note that you have to actually MAKE a legend with the legend function, or you won’t see the label. e.g `label=”2011 marks”`

**Graph Decoration Functions** – use these AFTER you’ve used a graph generation function. Not all will work with every type of graph.
--------------------

**grid(kwargs)**
<br />Set up a grid on your plot – normally only used with plot graphs. 
<br />Some kwargs:
*	`linestyle`, linewidth, color: as for plot
*	`zorder`: see [zorder in matplotlib explanation](matplotlib.md) – especially important for a grid, which you really don’t want above your data.

**legend(kwargs)**
<br />Insert a legend for your plot. The legend appears inside the axes - use figlegend instead (not covered here) for a legend outside axes.
<br />Some kwargs:
*	`title`: a text-title for the legend e.g. title=”Locations”
*	`loc`: location for the legend – use `“upper left”`, `“center right”`, `“lower center”` etc. e.g. `loc=”lower right”`. Note the American spelling of center – centre will not work.
*	`numpoints`: Some versions of matplotlib show two copies of each symbol in the legend by default. 
I have no idea why they thought this was sensible, but use `numpoints=1` to correct it if you get it.

**subplots_adjust(kwargs)**
<br />This is potentially confusing! 
Subplots are a matplotlib concept we aren’t covering in this course, but are 
useful when dealing with complex many-part figures. However you can use one of the subplots 
functions to reposition your graph on the page, which is often useful (e.g. if your axis labels 
are vanishing off the bottom of the window), and that’s the only reason I’m mentioning this function here. 
If you’ve not set up any subplots, and you won't have in this course, then this `subplots_adjust` function will just work on whatever you have just plotted.
<br />Some kwargs: (values are in fractions of the page width/height)
*	`bottom`: position of bottom of chart – default is 0.1. e.g `bottom=0.2` (moves it up a bit, from 10% to 20% of page height)
*	`top`: position of top of chart – default is 0.9. e.g `top=0.95` (moves it up a bit to 95% of page height)
*	`left`: position of left of chart – default is 0.12 (12% of page width from left)
*	`right`: position of right of chart – default is 0.9 (90% of page width from left)

**text(x, y, text, kwargs)**
<br />Inserts text at a specified position. Use this to add arbitrary labels
<br />`x, y`: the position of the left of the text, in data coordinates
<br />`text`: string to display
<br />Some kwargs:
*	`fontsize`: set font size, in points. E.g. `fontsize=12`
*	`style`: set to `“italic”` for italic text
*	`weight`: set to `“bold”` for bold text
*	`color`: set text colour
*	`fontname`: set the font name. Be careful with these – a font that’s available on your computer might not be there on someone else’s. 
Font names are not case sensitive. e.g. `fontname=”times new roman”`.
*	`rotation`:  rotate text by a number in degrees – you call also use `“vertical”`. E.g. `rotation=45`.

**title(text, kwargs)**
<br />Sets the title of the plot to `text`` See `text` function for some kwargs.

**xlabel(text, kwargs)**
<br />**ylabel(text, kwargs)**
<br />Sets textual label for y-axis or x-axis to `text`. See `text` function for some kwargs.

**xlim(minx, maxx)**
<br />**ylim(miny, maxy)**
<br />Set minimum and maximum values for x and y on your plot – 
if you don’t do this, you get auto-selected values, which more often than not won't be precisely what you want (e.g. you’ll often want x and y to both start at 0).

**xticks(locations, labels, kwargs)**
**yticks(locations, labels, kwargs)**
<br />These two functions set the locations of, and text labels for, the ticks on the x and y axis. See `text` function for some kwargs that affect the text labels. 
`locations` is a list or array of numerical positions for the ticks that you want. 
`labels` is a list of strings to be used as labels. Text labels are optional – you can just provide locations.
e.g. `plt.xticks([1, 2, 3, 4],[“Spring”, ”Summer”, ”Autumn”, ”Winter”], rotation=”vertical”)`

**Graph Finalising Function** – use this when you’ve done with all graph setup
-----------------------

**show()**
<br />
The show function displays your graph/chart/plot in a new window, in which you can view it, or save it as a file. 
The program is paused until you close the window. After calling `show`, the graph is thrown away – calling more functions will start a new graph.
