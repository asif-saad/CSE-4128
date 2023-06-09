# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 23:37:12 2023

@author: USER
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('lena.jpg')
print(img.shape)


#%%
#gray = np.ones((128,128,3), dtype=np.uint8)
cv.imshow("Color",img)


b,g,r = cv.split(img)
#print(b.shape)
#cv.imshow("Green",g)
#cv.imshow("Red",r)
#cv.imshow("Blue",b)
r[:]=0
b[:]=0
merged = cv.merge((b,g,r))
#cv.imshow("Merged",merged )


#%%
image_bordered = cv.copyMakeBorder(src=img, top=25, bottom=25, left=25, right=25,borderType= cv.BORDER_CONSTANT)#BORDER_WRAP, cv.BORDER_REFLECT  
print(image_bordered.shape)
cv.imshow("Bordered",image_bordered )


#%%
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("GRAY", gray)

#%%
im = plt.imread("Lena.jpg")
gray = cv.cvtColor(im,cv.COLOR_BGR2GRAY)
plt.title("GRAY IMG")
plt.imshow(gray,"gray", vmin=0, vmax=255)
plt.show()


cv.waitKey(0)
cv.destroyAllWindows()