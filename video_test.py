import cv2
import time
import numpy as np
from detect import detect
from utils import print_position
 
if __name__ == '__main__' :
 
    time_to_run = 60 #seconds

    # Start default camera
    video = cv2.VideoCapture(0)
     
    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
     
    # With webcam get(CV_CAP_PROP_FPS) does not work.
    # Let's see for ourselves.
     
    if int(major_ver)  < 3 :
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else :
        fps = video.get(cv2.CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

     
    print("Capturing frames")
    num_frames = 0
 
    # Start time
    start = time.time()

    # Grab a few frames
    fps_show = 0

    while True:
        frame_start = time.time()
        ret, frame = video.read()
        if ret == True:
            h, w, _ = np.shape(frame)
            position = detect(frame)
            print_position(h, w, position, int(1/(time.time() - frame_start)))
            num_frames += 1
        if frame_start - start > time_to_run:
            break
 
     
    # End time
    end = time.time()

    # Time elapsed
    seconds = end - start
    print("Time taken : {0} seconds".format(seconds))
 
    # Calculate frames per second
    fps  = num_frames / seconds
    print("Estimated fps : {0}".format(fps))
 
    # Release video
    video.release()