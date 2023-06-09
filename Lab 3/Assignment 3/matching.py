import math
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

def erlang ():
    target=[0 for i in range (0,256)]
    k = int(input("k: "))
    miu = float(input("Miu: "))
    # k= 7
    # miu = .5
    for i in range (0,256):
        val = math.pow(i,k-1)
        val = val*math.exp(-(i/miu))
        x = math.pow(miu,k)*math.factorial(k-1)
        target[i] = val/x
    return target

x = erlang()



# plt.plot(x)

# plt.title("erlang distribution")

# plt.show()


#pdf of erlang distribution

sumOfDistribution = 0

for i in range (0,256):
    sumOfDistribution +=x[i]


print(sumOfDistribution)

PdfOfDistribution=[0 for i in range (0,256)]

for i in range(256):
    PdfOfDistribution[i] = x[i]/sumOfDistribution

# plt.plot(PdfOfDistribution)

# plt.title("pdf")

# plt.show()

#round CDF
CdfOfDistribution=[0 for i in range (0,256)]

CdfOfDistribution[0]=PdfOfDistribution[0]

for i in range(1,256):
    CdfOfDistribution[i] = CdfOfDistribution[i-1]+PdfOfDistribution[i]

for i in range(0,256):
    CdfOfDistribution[i] = round(CdfOfDistribution[i]*255)


# plt.plot(CdfOfDistribution)

# plt.title("cdf")

# plt.show()

imgInp = cv.imread('lena.png',cv.IMREAD_GRAYSCALE)


hist = [0 for i in range (0,256)]
pdf = [0 for i in range (0,256)]
cdf = [0 for i in range (0,256)]

totalPixels=imgInp.shape[0]*imgInp.shape[1]

for i in range (0,imgInp.shape[0]):
    for j in range (0,imgInp.shape[1]):
        m = imgInp[i][j]        
        hist[m]+=1
        
# plt.plot(hist)

# plt.title("histogram of input")

# plt.show()

#pdf

for i in range (0,256):
    pdf[i]=hist[i]/totalPixels

#cdf
  
cdf[0]=pdf[0]

for i in range (1,256):
    cdf[i]=cdf[i-1]+pdf[i]

for i in range(0,256):
    cdf[i] = round(cdf[i]*255)
    
# plt.plot(cdf)

# plt.title("cdf of input")

# plt.show()

# print(cdf)
# print(CdfOfDistribution)

map_ = [0 for i in range (0,256)]

for i in range (0,256):
    g = cdf[i]
    s = 0
    for j in range (s,256):
        if(CdfOfDistribution[j] >= g):
            map_[i] = j
            s = j
            break

#print(map_)

outImg = np.zeros(imgInp.shape)

for i in range (0,imgInp.shape[0]):
    for j in range (0,imgInp.shape[1]):
        m = imgInp[i][j]        
        outImg[i][j] = map_[m]

cv.imshow('input',imgInp) 
out = cv.normalize(outImg, None, 0, 1, cv.NORM_MINMAX)
cv.imshow('output',out) 

plt.figure(figsize=(15, 3))

plt.subplot(1, 3, 1)
plt.plot(x)
plt.title("Erlang distribution")

plt.subplot(1, 3, 2)
plt.hist(imgInp.ravel(),256,[0,255])
plt.title("Input histogram")

plt.subplot(1, 3, 3)
plt.hist(outImg.ravel(),256,[0,255])
plt.title("Output histogram")

plt.show()


cv.waitKey(0)
cv.destroyAllWindows()