import cv2
import numpy as np

img = cv2.imread('oc.jpg', 0)
r, img = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)#_INV)
cv2.imshow("Original", img)

kernel1 = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5)) #cv2.MORPH_RECT for all 1s
print(kernel1)
kernel1 = (kernel1) *255
kernel = np.uint8(kernel1)

rate = 50
kernel1 = cv2.resize(kernel, None, fx = rate, fy = rate, interpolation = cv2.INTER_NEAREST)
# cv2.imshow("kernel",kernel1)






# kernel = np.ones((25,25),np.uint8)

dilated = cv2.dilate(img,kernel,iterations = 1)
cv2.imshow("Dilation", dilated)

print(dilated.shape,img.shape)
val=cv2.bitwise_and(dilated,img)
print("value: ",val)


# eroded = cv2.erode(img,kernel,iterations = 1)
# cv2.imshow("Erosion", eroded)

# opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations = 1)
# cv2.imshow("Opening", opened)


# closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel,iterations =1)
# cv2.imshow("Closing", closed)




cv2.waitKey(0)
cv2.destroyAllWindows()