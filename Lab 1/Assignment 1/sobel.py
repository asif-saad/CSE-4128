import numpy as np
import cv2



img = cv2.imread('lena.jpg',cv2.IMREAD_GRAYSCALE)

kernel1 = np.array(( [-1,0,1],
                    [-2,0,2],
                    [-1,0,1]))

kernel2 = np.array(([-1,-2,-1],
                    [0,0,0],
                    [1,2,1]))


def conv(img,kernel):
        
    padding_y = (kernel.shape[0] - 1)//2 # 1
    padding_x = (kernel.shape[1] - 1)//2 # 2

    image_bordered = cv2.copyMakeBorder(src=img, top=padding_y,bottom=padding_y,left=padding_x,right=padding_x,borderType= cv2.BORDER_CONSTANT)
    out=np.zeros((img.shape[0],img.shape[1]))
    #out = img.copy()
    # cv2.imshow('bordered image',image_bordered)
    # cv2.waitKey(0)
    print(img.shape)
    print(image_bordered.shape)

    for y in range(padding_y,image_bordered.shape[0]-padding_y):
        for x in range(padding_x,image_bordered.shape[1]-padding_x):
            # mat = image_bordered[x:x+kernel2.shape[0],y:y+kernel2.shape[1]]
            # out [x,y]=np.sum(mat*kernel2)/255
            temp = 0
            for j in range(-padding_y, padding_y+1):
                for i in range(-padding_x, padding_x+1):
                    temp += kernel[j+padding_y][i+padding_x] * image_bordered[y-j][x-i]
            out[y-padding_y,x-padding_x] = temp
    print(out.shape)
    return out

out1 = conv(img,kernel1)
temp1 = cv2.normalize(out1, None, 0, 1, cv2.NORM_MINMAX)
out2 = conv(img,kernel2)
temp2 = cv2.normalize(out2, None, 0, 1, cv2.NORM_MINMAX)
cv2.imshow('input image',img)
cv2.imshow('Vertical Edge',temp1)
cv2.imshow('Horizontal Edge',temp2)

out3 = out1+out2
temp3 = cv2.normalize(out3, None, 0, 1, cv2.NORM_MINMAX)
cv2.imshow('All Edge',temp3)

lapKarnel = np.array(([0,-1,0],
                    [-1,4,-1],
                    [0,-1,0]))

out4 = conv(img,lapKarnel)
temp4 = cv2.normalize(out4, None, 0, 1, cv2.NORM_MINMAX)
cv2.imshow('laplacian filter',temp4)

cv2.waitKey(0)
cv2.destroyAllWindows()

