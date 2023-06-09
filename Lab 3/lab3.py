import cv2
import numpy as np
import matplotlib.pyplot as plt

img_inp = cv2.imread('landscape.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('input',img_inp)
img_out = np.zeros((img_inp.shape[0],img_inp.shape[1]))

totalPixel = img_inp.shape[0]*img_inp.shape[1]

Hist = [0 for i in range (0,256)]
cdf = [0 for i in range (0,256)]
s = [0 for i in range (0,256)]
Hist2 = [0 for i in range (0,256)]
cdf2 = [0 for i in range (0,256)]

#print(Hist)

for i in range (0,img_inp.shape[0]):
    for j in range (0,img_inp.shape[1]):
        x = img_inp[i][j]
        Hist[x]+=1
        

#print(Hist)

#pdf
for i in range (0,256):
    Hist[i] = Hist[i]/totalPixel

#CDF
sum_Hist=0
for i in range(0,256):
    sum_Hist = sum_Hist+Hist[i]
    cdf[i]=sum_Hist
    s[i] = round(cdf[i]*255)

# print(cdf)    
#print(s)

#Output
for i in range (0,img_inp.shape[0]):
    for j in range (0,img_inp.shape[1]):
        x = img_inp[i][j]
        img_out[i][j] = s[x]

#print(Hist)

for i in range (0,img_out.shape[0]):
    for j in range (0,img_out.shape[1]):
        x = img_out[i][j]
        Hist2[int(x)]+=1

#pdf
for i in range (0,256):
    Hist2[i] = Hist2[i]/totalPixel

#CDF
sum_Hist=0
for i in range(0,256):
    sum_Hist = sum_Hist+Hist2[i]
    cdf2[i]=sum_Hist

out = cv2.normalize(img_out, None, 0, 1, cv2.NORM_MINMAX)
cv2.imshow('output',out) 

#histr = cv2.calcHist([img_inp],[0],None,[256],[0,256])
# plt.plot(cdf)
# plt.title("CDF input")
# plt.show()

# plt.plot(cdf2)
# plt.title("CDF output")
# plt.show()


plt.figure(figsize=(20, 4))

plt.subplot(1, 4, 1)
plt.title("Input Image Histogram")
plt.hist(img_inp.ravel(),256,[0,255])


plt.subplot(1, 4, 2)
plt.plot(cdf)
plt.title("CDF input")


plt.subplot(1, 4, 3)
plt.title("output Image Histogram")
plt.hist(img_out.ravel(),256,[0,255])

plt.subplot(1, 4, 4)
plt.plot(cdf2)
plt.title("CDF output")
plt.show()


      

cv2.waitKey(0)
cv2.destroyAllWindows()