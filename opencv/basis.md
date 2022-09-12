# Here is the example

```
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
- `cv2.IMREAD_UNCHANGED or -1` 
- `cv2.IMREAD_GRAYSCALE or 0`
- `cv2.IMREAD_COLOR or 1` 

But the default value for flags is 1, which will read in the image as a Colored image
## Displaying an Image
```
imshow(window_name,  image)
```
`window_name` is the window name that will be displayed on the window
`image` is the image that you want to display

The `imshow` is designed to be used along with the `waitKey(0)` and `destroyAllWindows` or `destroyWindow()` function.
If 0 is passed, the program waits indefinitely for a keystroke.
