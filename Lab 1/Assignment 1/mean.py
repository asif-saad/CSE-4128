import numpy as np
import cv2



img = cv2.imread('lena.jpg',cv2.IMREAD_GRAYSCALE)

kernel = np.array(( [1,1,1],
                    [1,1,1],
                    [1,1,1] ))

print(np.sum(kernel))
kernel=kernel/25


# kernel2 = np.array(( [1,0,-1],
#                     [2,0,-2],
#                     [1,0,-1]))

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



out = conv(img,kernel)
out = cv2.normalize(out, None, 0, 1, cv2.NORM_MINMAX)
cv2.imshow('input image',img)
cv2.imshow('result image',out)
cv2.waitKey(0)
cv2.destroyAllWindows()


