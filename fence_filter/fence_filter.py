import cv2 as cv

import numpy as np

 

cap = cv.VideoCapture("C:\\Users\\ijeff\\Downloads\\RunIn.mp4")

mask = cv.imread('fence_mask2.png',0)

mask = cv.resize(mask, (513,288), interpolation = cv.INTER_AREA)

video = cv.VideoWriter('lion_defenced.mp4',cv.VideoWriter_fourcc(*'MP4V'),30,(513,288))

while(cap.isOpened()):

    ret, frame = cap.read()

    if ret==True:

        frame = cv.resize(frame, (513,288), interpolation = cv.INTER_AREA)

        # dst = cv.inpaint(frame,mask,3,cv.INPAINT_TELEA)

        dst = cv.inpaint(frame,mask,3,cv.INPAINT_NS)

 

        video.write(dst)

        key = cv.waitKey(30)

        if key == 27 or key == 'q':

            cont = False

            break

    else:

        break

 

cap.release()

video.release()

cv.destroyAllWindows()