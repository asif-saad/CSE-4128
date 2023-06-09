import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math

g_a = np.zeros(256,np.float32)

m_a = 80.0

sd_a = 35.0

for i in range(256):
    r = i-m_a
    r = r*r
    r = r/(sd_a*sd_a)
    r = math.exp(-(r))
    r = r/(sd_a*math.sqrt(2*3.1416))
    g_a[i] = r
    
plt.plot(g_a)

plt.title("Gaussian function 1")

plt.show()

g_b = np.zeros(256,np.float32)

m_b = 200.0

sd_b = 20.0

for i in range(256):
    r = i-m_b
    r = r*r
    r = r/(sd_b*sd_b)
    r = math.exp(-(r))
    r = r/(sd_b*math.sqrt(2*3.1416))
    g_b[i] = r
    
plt.plot(g_b)

plt.title("Gaussian function 2")

plt.show()

gauss = g_a+g_b

plt.plot(gauss)

plt.title("Added Gaussian function")

plt.show()