import numpy as np
import cv2
import matplotlib.pyplot as plt

img =  cv2.imread("lena.png",cv2.IMREAD_GRAYSCALE)

width, height = img.shape

angle = float(input("Angle: "))
Yl = float(input("Gamma Low: "))
Yh = float(input("Gamma High: "))
c = float(input("C: "))
d0 = float(input("D0: ")) 
# Yl = .4
# Yh =2
# c =1.2
# d0 = 10

x = np.linspace(0,1,height)
y = np.linspace(0,1,width)
xx, yy = np.meshgrid(x, y)

# print(xx)
# print(yy)
# print(xx+yy)

illum_pattern = np.cos(np.deg2rad(angle)) * xx + np.sin(np.deg2rad(angle)) * yy

# print(illum_pattern)

illum_pattern -= illum_pattern.min()
illum_pattern /= illum_pattern.max()

noisy_img = cv2.normalize(np.multiply(img, illum_pattern), None, 0, 1, cv2.NORM_MINMAX)

noisy_img1 = np.log1p(noisy_img)

f = np.fft.fft2(noisy_img1)
shift = np.fft.fftshift(f)
m = np.abs(shift)
a = np.angle(shift)

H = np.zeros(noisy_img1.shape)
for u in range(noisy_img1.shape[0]):
    for v in range(noisy_img1.shape[1]):
        i = (u - noisy_img1.shape[0]//2)**2
        j = (v - noisy_img1.shape[1]//2)**2
        r = np.exp(-((c*(i+j))/(2*d0**2)))
        r = (Yh-Yl) *(1-r) + Yl
        H[u][v] = r

m = m*H

filtered_image = np.multiply(m,np.exp(1j*a)) 
filtered_image = np.fft.ifftshift(filtered_image)
filtered_image = np.real(np.fft.ifft2(filtered_image))
filtered_image = np.exp(filtered_image)-1
filtered_image = cv2.normalize(filtered_image, None, 0, 1, cv2.NORM_MINMAX)


f0 = plt.figure(7)
plt.imshow(img,'gray')
plt.title('Input')

f1 = plt.figure(1)
plt.imshow(np.log(np.abs(shift)),'gray')
plt.title('Magnitude of noisy_img')

f2 = plt.figure(2)
plt.imshow(illum_pattern,'gray')
plt.title('Illumination Pattern')

f3 = plt.figure(3)
plt.imshow(noisy_img, 'gray')
plt.title('noisy_img')

f4 = plt.figure(4)
plt.imshow(H,'gray')
plt.title('Filter')

f5 = plt.figure(5)
plt.imshow(np.log(m),'gray')
plt.title('Magnitude of filtered_image')

f6 = plt.figure(6)
plt.imshow(filtered_image,'gray')
plt.title('Output')

plt.show()
