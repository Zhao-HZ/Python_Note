# Here is the example
```python
import cv2 as cv

vid_capture = cv.VideoCapture('./res/test.mp4')

if vid_capture.isOpened() == False:
    print('Error')
else:
    # Get frame rate information
    fps = vid_capture.get(5)
    print('Frames per second: ', fps, 'FPS')
    frame_count = vid_capture.get(7)
    # frame_count = vid_capture.get(CAP_PROP_FRAME_COUNT)
    print('Frame count: ', frame_count)

while vid_capture.isOpened():
    ret, frame = vid_capture.read()
    if ret == True:
        cv.imshow('Frame', frame)
        key = cv.waitKey(20)
        # ord('q') is 113 which is the ASCII code for q key
        if key == ord('q'): # or if key == 113:
            break
    else:
        break

vid_capture.release()
cv.destroyAllWindows()
```
## Reading Video From a File
`VideoCapture(path, apiPreference)` 
It can create a `VideoCapture` object
`path` is the filename/path to the video file
`apiPreference` is optional
Create a video object.
`vid_capture = cv.VideoCapture('./res/test.mp4')`
Then we can use the `isOpened()` method to confirm the video file was opened  successfully
Assuming the video file was opened successfully,we can use the `get()` method to retrive important metadata associated with the video stream.
Notice that this method does not apply to web cameras.
In the example, 5 and 7 correspond to the frame rate(CAP_PROP_FPS) and frame count(CAP_PROP_FRAME_COUNT).
```python
fps = vid_capture.get(5) # Get frame rate information
frame_count = vid_capture.get(7) # Get frame count
```
In order to read each image frame from the file, we creat a loop and read one frame at a time from the video stream using the `vid_capture.read()` method which returns a tuple, <u>where the first element is a boolean and the next element is the actual video frame<u>.
<u>when the first element is true, it indicates the video stream contains a frame to read</u>
At the end you need to release the Video_Capture object and close the window
```python
vid_capture.release()
cv.destroyAllWindows()
```
## Reading an Image Sequence
## Reading Video from a Webcam
You need to give a video capture device index, as shown below
- If your system has a built-in webcam, then device index == 0 
- If you have more than one camera connected to your system, then the device index associated with each additional camera is incremented(e.g. 1, 2, etc)
```pyhton
vid_capture = cv.VideoCapture(0, cv.CAP_DSHOW)
```
`CAP_DSHOW` is an optional argument, it is short for directshow via video input

## Writing the Video
- Retrieve the image frame height and width,using the `get()` method
- Initialize a video capture object, to read the video stream into memory, using any of the sources previously described
- Create a video writer object.
- Use the video write object to save the video stream to disk.
``` python
# Obtain frame size information using get() method
frame_width = int(vid_capture.get(3)) # CAP_PROP_FRAME_WIDTH    
frame_height = int(vid_capture.get(4)) # CAP_PROP_FRAME_HEIGHT
frame_size = (frame_width,frame_height)
fps = 20
```
## Syntax
```
VideoWriter(filename, apiPreference, fourcc, fps, frameSize[, isColor])
```
- filename: pathname for the output video file
- apiPreference:  API backends identifier
- fourcc: 4-character code of codec, used to compress the frames (fourcc)
- fps: Frame rate of the created video stream
- frame_size: Size of the video frames
- isColor: If not zero, the encoder will expect and encode color frames. Else it will work with grayscale frames (the flag is currently supported on Windows only).
For second argument for VideoWriter
```py
VideoWriter_fourcc('M', 'J', 'P', 'G') # AVI 
VideoWriter_fourcc(*'XVID') # MP4
```
How to initialize video writer object
```py
output = cv2.VideoWriter('Resources/output_video_from_file.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 20, frame_size)
```
```py
while(vid_capture.isOpened()):
    # vid_capture.read() methods returns a tuple, first element is a bool
    # and the second is frame
    ret, frame = vid_capture.read()
    if ret == True:
           # Write the frame to the output files
           output.write(frame)
    else:
         print('Stream disconnected')
           break
vid_capture.release()
output.release()
```