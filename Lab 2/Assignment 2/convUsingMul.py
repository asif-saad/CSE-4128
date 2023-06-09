import numpy as np
import cv2

img = cv2.imread('lena128.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('inp',img)
cv2.waitKey(0)
outImg = img.copy()

img_row,img_col = img.shape     


karnel = np.array(( [1,1,1],
                    [1,1,1],
                    [1,1,1] ))

karnel = karnel/9

KRow,kCol = karnel.shape
out_row = img_row + KRow -1
out_col = img_col + kCol - 1
outImg = np.zeros([out_row,out_col])

karnelMod = np.pad(karnel, ((out_row - KRow, 0),(0, out_col - kCol)),'constant', constant_values=0) 
#print(karnelMod.shape)

toeplitz_list = []
for i in range(karnelMod.shape[0]-1, -1, -1):  
    first_col = karnelMod[i, :]
    #print(first_col.shape)  
    toeplitz_m = np.zeros((first_col.shape[0],img_col))
    for rangeRow in range(0,toeplitz_m.shape[1]):      
        for rangeCol in range(0,toeplitz_m.shape[0]):
            #print(rangeCol+rangeRow)
            if rangeCol+rangeRow<first_col.shape[0]:    
                toeplitz_m[rangeCol+rangeRow][rangeRow]=first_col[rangeCol]
    #print(toeplitz_m)            
    toeplitz_list.append(toeplitz_m)
                 

doubly_index = np.zeros((karnelMod.shape[0],img_row))
for r in range(0,doubly_index.shape[1]):
    for c in range (0,doubly_index.shape[0]):
        if r+c<doubly_index.shape[0]:
            doubly_index[r+c][r] = c+1
#print(doubly_index)   
toeplitz_shape = toeplitz_list[0].shape # shape of one toeplitz matrix
#print(toeplitz_shape)
doubly_row = toeplitz_shape[0]*doubly_index.shape[0]
doubly_col = toeplitz_shape[1]*doubly_index.shape[1]
print(doubly_row,doubly_col)
    
doubly_blocked_shape = [doubly_row, doubly_col]
doubly_blocked = np.zeros(doubly_blocked_shape)
b_h, b_w = toeplitz_shape 
for i in range(doubly_index.shape[0]):
    for j in range(doubly_index.shape[1]):
        start_i = i * b_h
        start_j = j * b_w
        end_i = start_i + b_h
        end_j = start_j + b_w
        doubly_blocked[start_i: end_i, start_j:end_j] = toeplitz_list[int(doubly_index[i,j]-1)]
        #print(doubly_blocked)

print(doubly_blocked.shape)

col_row = img.shape[0]*img.shape[1]     
col_vector = [[0 for i in range(0,1)] for j in range(0,col_row)]
row_element = 0 
i = img.shape[0]    
while i>0 :
    for j in range(0,img.shape[1]):
        col_vector[row_element][0] = img[i-1][j]
        row_element += 1
    i -= 1
#print(col_vector)

res_vector = np.matmul(doubly_blocked,col_vector)
print(res_vector.shape)


row_element =0 
for i in range(out_row):
    for j in range(out_col):
        outImg[i][j] = res_vector[row_element]
        row_element += 1    
outImg=np.flipud(outImg)
#print(outImg)
print(np.min(outImg),np.max(outImg))
out = cv2.normalize(outImg, None, 0, 1, cv2.NORM_MINMAX)
#print(outImg)
cv2.imshow('inp',img)
cv2.imshow('out',out)
cv2.waitKey(0)
cv2.destroyAllWindows()