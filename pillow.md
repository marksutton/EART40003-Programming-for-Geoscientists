PIL (Python Image Library) is a module providing image manipulation functionality. It can do all sorts of things, but we 
will use it in its simplest form – to read an image file into a numpy array so we can manipulate it, then to write that array back
out as a file. To use PIL.image, it’s normal to import it as:

<pre>
from PIL import Image         # standard import line for PIL.image
</pre>

To read an image file into a numpy array:

<pre>
img = Image.open("imagefile.png")  # read the image into array im
image_as_array = np.array(img)
</pre>

or just

<pre>
image_as_array = np.array(Image.open("imagefile.png")  )
</pre>

To write an array out as an image:

<pre>
img = Image.fromarray(array_to_write_as_image)
img.save("filename.png")
</pre>

or just

<pre>
Image.fromarray(array_to_write_as_image).save("filename.png")
</pre>

PIL.Image knows about a lot of formats, so should work with png, jpg, bmp, tiff and most common image types (but not all – there are a LOT of image formats out there). 

Array shapes and formats:
------------------------

If the image is a greyscale image, the data will be a 2D array – first dimension is height, second dimension is width. Vertical positions are counted from the top, not the bottom, so [0,0] is the top left corner, [0,1] is one pixel to the right of the top left corner. Each value will be a pixel intensity, 0-255. If the image is a RGB (colour) image, you get an extra dimension of size 3 – these are the red, green and blue levels, using the same 0-255 scale. So [10, 20, 1] gives you the green value at position 10 pixels from the top, 20 pixels from the left.
