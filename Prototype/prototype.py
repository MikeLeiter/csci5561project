# Code for prototype

import cv2 as cv

import numpy as np

 

cap = cv.VideoCapture("C:\\Users\\ijeff\\Documents\\csci5561\\DeepLabCut\\Lion_trim_sub.mp4")

blur = 1

_, first_frame = cap.read()

first_gray = cv.cvtColor(first_frame, cv.COLOR_BGR2GRAY)

first_gray = cv.GaussianBlur(first_gray, (blur, blur), 0)

height,width,layers = first_frame.shape

 

video = cv.VideoWriter('Lion_bg_sub_test.avi',cv.VideoWriter_fourcc(*'MJPG'),30,(width,height))

cont = True

while cont:

    _, frame = cap.read()

    try:

        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        gray_frame = cv.GaussianBlur(gray_frame, (blur, blur), 0)

    except:

        break

 

    difference = cv.absdiff(first_gray, gray_frame)

    _, difference = cv.threshold(difference, 9, 255, cv.THRESH_BINARY)

    final = cv.bitwise_and(frame, frame, mask = difference)

    dst = cv.medianBlur(final,5)

    video.write(dst)

 

 

    key = cv.waitKey(30)

    if key == 27 or key == 'q':

        cont = False

        break

 

cap.release()

video.release()

cv.destroyAllWindows()