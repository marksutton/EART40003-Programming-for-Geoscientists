# PIL.Image module

Pillow is an image-manipulation library which, for historical reasons, is imported in Python using the name PIL. It can do all sorts of things, but we will use it in its simplest form – to read an image file into a *NumPy* array so we can manipulate it, then to write that array back out as a file. To use PIL.Image, it’s normal to import it as:

```python
from PIL import Image         # standard import line for PIL.image
```

To read an image file into a NumPy array:

```python
img = Image.open("imagefile.png")  # open the image file
image_as_array = np.array(img)
```

or just

```python
image_as_array = np.array(Image.open("imagefile.png")  )
```

To write an array out as an image:

```python
img = Image.fromarray(array_to_write_as_image)
img.save("filename.png")
```

or just

```python
Image.fromarray(array_to_write_as_image).save("filename.png")
```

PIL.Image knows about a lot of formats, so should work with png, jpg, bmp, tiff and most common image types (but not *all* – there are a LOT of image formats out there).

Array shapes and formats:

If the image is a greyscale image, the data will be a 2D array – first dimension is height, second dimension is width. Vertical positions are counted from the top, not the bottom, so [0,0] is the top left corner, [0,1] is one pixel to the right of the top left corner. Each value will be a pixel intensity, 0-255. If the image is a RGB (colour) image, you get an extra dimension of size 3 – these are the red, green and blue levels, using the same 0-255 scale. So [10, 20, 1] gives you the green value at position 10 pixels from the top, 20 pixels from the left.

See [NumPy arrays](numpy.md) for working with the arrays used here.

[Return to the site index](index.md)
