import numpy as np

# print(np.__version__)
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
# print('The dim of array:',array1d.ndim)

# print(array2d.base)# return None if the array owns data like copy,asign,etc,    not view and shape
# print(array1d.shape)# The shape of an array is the number of elements in the each dimension

# new_array = array1d.reshape(2,2,4)# reshape the array to change dimension of array and shape of it 
# new_array = array1d.reshape(2,2,-1)# other way to reshape array, auto cacul
# print(array3d,end='\n\n')
# new_array = array3d.reshape(-1)
# print(array3d)
# for i in np.ndenumerate(array3d): 
#     print(i)

# filter_arr = array1d %2 ==1
# new_arr = array1d[filter_arr]

# print(new_arr)
# x = np.random.rand(2,3) # Return a array with random element in range [0,1]
x = np.random.randint(100,size=(34)) #return a side() array with 4 element in range [0,100]
# x = np.random.randint(low=10,high=90,size=(9,7)) #return a array with the shape it's have
# x2 = np.random.choice(x,size=(9,7)) # choice a random element in the array if have size will create a array with the element from array

# print(x2)
            # import seaborn
            # import matplotlib.pyplot as plt

            # seaborn.distplot(x)

            # plt.show()


            # def sub(x, y,z):
            #     '''hàm tự tạo để tí dùng cho cái fromyfunc , not limit'''
            #     return x - y - z

            # list4 = np.frompyfunc(sub,3,1)

            # print(list4(list1,list2,list3))
            # print(np.add)

# while 1:
#     c = input('tiếp không: ')
#     ran = np.random.randint(100,size= 5)
#     print(ran)
#     ran1 = np.gcd.reduce(ran)
#     print('LCM is:',ran1)
    
