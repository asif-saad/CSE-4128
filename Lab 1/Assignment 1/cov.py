import numpy as np
import cv2



img = cv2.imread('lena.jpg',cv2.IMREAD_GRAYSCALE)

cv2.waitKey(0)


kernel2 = np.array([[-1, 0, 1],
                    [-1, 0, 1],
                    [-1, 0, 1]])

image_bordered = cv2.copyMakeBorder(src=img, top=1, bottom=1, left=1, right=1,borderType= cv2.BORDER_CONSTANT)
out=np.zeros((image_bordered.shape[0],image_bordered.shape[1]))

for i in range(image_bordered.shape[0]-2):
    for j in range(image_bordered.shape[1]-2):
        mat = image_bordered[i:i+3,j:j+3]
        out [i,j]=np.sum(mat*kernel2)/255
        #print(out[i,j])

print(out)
cv2.imshow('result image',out)
cv2.waitKey(0)
cv2.destroyAllWindows()