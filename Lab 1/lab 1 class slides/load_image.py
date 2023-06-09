import numpy as np
import cv2



img = cv2.imread('lena.jpg',cv2.IMREAD_GRAYSCALE)

#out=img.copy()
out = np.zeros((512,512), dtype=np.uint8)
print(img.max())
print(img.min())

#cv2.imshow('output image',out)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        a = img.item(i,j)
        out.itemset((i,j),255-a)
        
cv2.imshow('output image',out)





kernel2 = np.array([[-1, -1, -1],
                    [-1, 8, -1],
                    [-1, -1, -1]])
  




cv2.waitKey(0)
cv2.destroyAllWindows()





#cv2.normalize(src,des, 0, 255, cv2.NORM_MINMAX)
#s = np.round(s).astype(np.uint8)