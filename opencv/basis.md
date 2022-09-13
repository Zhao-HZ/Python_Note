
# Here is the example

```python
import cv2 as cv

img_gray_scale = cv.imread('test.jpg', 0)

cv.imshow('grayscale image', img_gray_scale)

cv.waitKey(0)

cv.destroyAllWindows()

cv.imwrite('grayscale.jpg', img_gray_scale)
```

## Reading an Image

```
cv.imread(filename, flags)
```

`filename` is a qualified pathname to the file
`flags` is an <u>optional</u> flag that lets you specify how the image should be represented.
There are two flags

- cv2.IMREAD_UNCHANGED or -1 
- cv2.IMREAD_GRAYSCALE or 0 
- cv2.IMREAD_COLOR or 1 

But the default value for flags is 1, which will read in the image as a Colored image

## Displaying an Image

```python
imshow(window_name,  image)
```

`window_name` is the window name that will be displayed on the window
`image` is the image that you want to display

## Write an Image
```
imwrite(filename, image)
```
`filename` is a filename, which must include the filename extension(png, jpg).
`image` is the image you want to save.The function returns True if the image is saved successfully.