# -*- coding: utf-8 -*-
"""
Created on Sun May 10 17:12:19 2020

@author: bajrang
"""
import cv2
img= cv2.imread('img.jpg',0)
#img= cv2.imread('img.jpg')
#gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('grauscale img',img)
#cv2.imshow('original img',img)
#cv2.imwrite('output.jpeg',img)
#cv2.imwrite('output.png',img)
#print(img.shape)
cv2.waitKey(0)
ret,bw=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow("binary image", bw)
cv2.waitKey(0)
cv2.destroyAllWindows()




