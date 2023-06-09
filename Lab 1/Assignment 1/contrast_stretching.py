import numpy as np
import cv2

img = cv2.imread('contrast.tif',cv2.IMREAD_GRAYSCALE)
out=img.copy() 

max_val=out.max()
min_val=out.min()

print(max_val,min_val)
#cv2.imshow('input image',img)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        a = img.item(i,j)
        c=((a-min_val)/(max_val-min_val+1))*255
        out.itemset((i,j),c)
        
cv2.imshow('output image',out)
print(out.max())
print(out.min())
cv2.imshow('input image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()