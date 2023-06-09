import numpy as np
from scipy.linalg import toeplitz as tplz

arr = np.array(([10,20],[30,40]))

resArr = np.pad(arr,((1,0),(0,2)),'constant',constant_values=0)
#print(resArr)

def toeplitz_each(zpfkernel,img_col):
    toeplitz_list = []
    for i in range(zpfkernel.shape[0]-1, -1, -1):   # iterate from last row to the first row
        first_col = zpfkernel[i, :]
        print(first_col.shape)# i th row of the F 
        # first_row = np.r_[first_col[0], np.zeros(img_col-1)] # first row for the toeplitz fuction should be defined otherwise
        # #print(first_row)
        #                                                 # the result is wrong
        # toeplitz_m = tplz(first_col,first_row)          # toeplitz function is in scipy.linalg library
        # #print(toeplitz_m)
        toeplitz_m = np.zeros((first_col.shape[0],img_col))
        for rangeRow in range(0,toeplitz_m.shape[1]):      
            for rangeCol in range(0,toeplitz_m.shape[0]):
                #print(rangeCol+rangeRow)
                if rangeCol+rangeRow<first_col.shape[0]:    
                    toeplitz_m[rangeCol+rangeRow][rangeRow]=first_col[rangeCol]
        toeplitz_list.append(toeplitz_m)
        #print(toeplitz_m)
    return toeplitz_list

def doubly_toeplitz(zpfkernel,tplz_list,img_row):
    # doubly blocked toeplitz indices: 
    # this matrix defines which toeplitz matrix from toeplitz_list goes to which part of the doubly blocked
    print(zpfkernel)
    print(zpfkernel.shape)
    doubly_indices = np.zeros((zpfkernel.shape[0],img_row))
    for r in range(0,doubly_indices.shape[1]):
        for c in range (0,doubly_indices.shape[0]):
            if r+c<doubly_indices.shape[0]:
                doubly_indices[r+c][r] = c+1
    print(doubly_indices)
    
    ## creat doubly blocked matrix with zero values
    toeplitz_shape = tplz_list[0].shape # shape of one toeplitz matrix
    print(toeplitz_shape)
    doubly_row = toeplitz_shape[0]*doubly_indices.shape[0]
    doubly_col = toeplitz_shape[1]*doubly_indices.shape[1]
    print(doubly_row,doubly_col)
    
    doubly_blocked_shape = [doubly_row, doubly_col]
    doubly_blocked = np.zeros(doubly_blocked_shape)
    # tile toeplitz matrices for each row in the doubly blocked matrix
    b_h, b_w = toeplitz_shape # hight and witghs of each block
    for i in range(doubly_indices.shape[0]):
        for j in range(doubly_indices.shape[1]):
            start_i = i * b_h
            start_j = j * b_w
            print(start_i,start_j)
            end_i = start_i + b_h
            end_j = start_j + b_w
            print(end_i,end_j)
            doubly_blocked[start_i: end_i, start_j:end_j] = tplz_list[int(doubly_indices[i,j]-1)]
    print(doubly_blocked)
    return doubly_blocked
def input_to_column_vect(img_inp):
    col_row = img_inp.shape[0]*img_inp.shape[1]     #take the row size
    col_vector = [[0 for i in range(0,1)] for j in range(0,col_row)]    #intialize the column vectorwith zero
    row_element = 0 #to iterate trhough the rows in column vector
    i = img_inp.shape[0]    
    while i>0 :
        for j in range(0,img_inp.shape[1]):
            col_vector[row_element][0] = img_inp[i-1][j] # fill the column vector with the values of input row from bottom to up 
            row_element += 1
        i -= 1
    return col_vector

x = toeplitz_each(resArr,3)
doubly_toeplitz(resArr,x,2)

