import numpy as np
import cv2 



img = cv2.imread('lena.jpg',cv2.IMREAD_GRAYSCALE)
print(img)
outGama=np.zeros((img.shape[0],img.shape[1]), dtype=np.uint8)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        r = img.item(i,j)
        y = 2
        c=1/pow(255,y-1)
        r = pow(r,y)
        outGama[i][j] = (c*r)
        
print(outGama)

cv2.imshow('Output Image(gama)',outGama)

cv2.imshow('Input Image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()