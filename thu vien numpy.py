# import numpy as np

# # print(np.__version__)
# fuck = [1,2,3,5,5,4,54,5,4,54,5,4,5,45,4,4]
# nga = [7,9,0,10]
# dang = [12,13,14,15]
# than = [17,13,19,20]
# vu = [43,43,45,34]

# array1d = np.array(fuck)
# array1d1 = np.array(nga)
# array2d = np.array([nga,dang,than])
# array3d = np.array([[dang,than],[nga,vu]])

# # print(array1d)
# # print('The dim of array:',array1d.ndim)

# # print(array2d.base)# return None if the array owns data like copy,asign,etc,    not view and shape
# # print(array1d.shape)# The shape of an array is the number of elements in the each dimension

# # new_array = array1d.reshape(2,2,4)# reshape the array to change dimension of array and shape of it 
# # new_array = array1d.reshape(2,2,-1)# other way to reshape array
# # print(array3d,end='\n\n')
# # new_array = array3d.reshape(-1)
# # print(array3d)
# # for i in np.ndenumerate(array3d): 
# #     print(i)

# filter_arr = array1d %2 ==1
# new_arr = array1d[filter_arr]

# print(new_arr)


import os
print(os.getcwd())