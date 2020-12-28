# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:31:32 2020

@author: bajrang
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May 10 17:12:19 2020

@author: bajrang
"""
import cv2
img= cv2.imread('img.jpg')
img_HSV=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('hsv image', img_HSV)

cv2.imshow('hue image', img_HSV[ :, :,0])
cv2.imshow('channel image', img_HSV[:,:,1])
cv2.imshow('saturation image', img_HSV[:,:,2])


cv2.waitKey(0)
cv2.destroyAllWindows()




