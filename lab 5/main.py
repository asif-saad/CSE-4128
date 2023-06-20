import numpy as np
import matplotlib
import cv2
import matplotlib.pyplot as plt

point_list=[]

img = cv2.imread('img2.jpg', 0)
_,img_actual=cv2.threshold(img,130,1,cv2.THRESH_BINARY)
_,img_inv=cv2.threshold(img,130,1,cv2.THRESH_BINARY_INV)


# click and seed point set up
x = None
y = None

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(20,20)) #cv2.MORPH_RECT for all 1s
#print(kernel1)



# The mouse coordinate system and the Matplotlib coordinate system are different, handle that
def onclick(event):
    global x, y
    ax = event.inaxes
    if ax is not None:
        x, y = ax.transData.inverted().transform([event.x, event.y])
        x = int(round(x))
        y = int(round(y))
        
        point_list.append((x,y))
        
        

        
        
         

X = np.zeros_like(img)
plt.title("Please select seed pixel from the input")
im = plt.imshow(img, cmap='gray')
im.figure.canvas.mpl_connect('button_press_event', onclick)
plt.show(block=True)


X[point_list[0][0]][point_list[0][1]]=1
cnt=1
while True:
    temp=cv2.dilate(X,kernel,iterations=1)
    temp=cv2.bitwise_and(temp,img_inv)
    
    if(np.array_equal(temp,X)):
        break
    
    X=temp
    cnt+=1
    
print(cnt)    
output=cv2.bitwise_or(X,img_actual)
plt.imshow(output,cmap='gray')
plt.show()
    
    
    
    
    
    
    