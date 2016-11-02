# -*- coding: utf-8 -*-
from __future__ import print_function

import cv2
import numpy as np

#read the image in grayscale & show
img = cv2.imread('banner.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('img', img)

#make a blach/white copy of the image & show
thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)[1]
cv2.imshow('thresh',thresh)

#make a copy of the image, find the contours & show
imgcopy = np.copy(img)
contours = cv2.findContours(imgcopy, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
cv2.imshow('contours',contours)

#wait for keyinput and then destroy all shows
cv2.waitKey(0)
cv2.destroyAllWindows()