# Fourier transform - guassian lowpass filter

import cv2
import numpy as np
from matplotlib import pyplot as plt
from copy import deepcopy as dpc



def min_max_normalize(img_inp):
    inp_min = np.min(img_inp)
    inp_max = np.max(img_inp)

    for i in range (img_inp.shape[0]):
        for j in range(img_inp.shape[1]):
            img_inp[i][j] = (((img_inp[i][j]-inp_min)/(inp_max-inp_min))*255)
    return np.array(img_inp, dtype='uint8')

# take input
img_input = cv2.imread('input.jpg', 0)

img = dpc(img_input)

image_size = img.shape[0] * img.shape[1]

# fourier transform
ft = np.fft.fft2(img)

ft_shift = np.fft.fftshift(ft)

magnitude_spectrum_ac=np.abs(ft_shift)
magnitude_spectrum = 1 * np.log(np.abs(ft_shift)+1)
magnitude_spectrum_scaled = min_max_normalize(magnitude_spectrum)

#mag, ang = cv2.cartToPolar(ft_shift[:,:,0],ft_shift[:,:,1])
ang = np.angle(ft_shift)

## phase add



#cw
filter_ = np.full(img_input.shape,1,dtype=np.int32)
#print(filter_)
x,y=filter_.shape
cx = int(input("X:"))
cy = int(input("Y:"))
r = int(input("R:"))

for i in range (-r,r+1):
    for j in range (-r,r+1):
        dis = (0-i)**2+(0-j)**2
        if(dis<=r**2):
            filter_[cx+i][cy+j]=0
            

cv2.imshow('output filter',min_max_normalize(filter_)) 

r = np.multiply(filter_,magnitude_spectrum_ac)
cv2.imshow('output',min_max_normalize(r)) 

final_result = np.multiply(r, np.exp(1j*ang))
# inverse fourier
img_back = np.real(np.fft.ifft2(np.fft.ifftshift(final_result)))
img_back_scaled = min_max_normalize(img_back)

## plot
cv2.imshow("input", img_input)
cv2.imshow("Magnitude Spectrum",magnitude_spectrum_scaled)

cv2.imshow("Phase",ang)
cv2.imshow("Inverse transform",img_back_scaled)



cv2.waitKey(0)
cv2.destroyAllWindows() 
