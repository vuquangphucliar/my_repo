nhiphan=[]
a=int(input('Nhập 1 số bất kì : ' ))
while(a!=0):
    du=a%2
    nhiphan.append(du)#                 BÀI NÀY CỦA THẦY 
    a=a//2#                     DÙNG PHÉP CHIA LẤY PHẦN NGUYÊN 

print('Số lần con 1 xuất hiện là',nhiphan.count(1))                        #CÁCH NÀY KHÓ HIỂU PHẾT
print("Dạng nhị phân của nó là",end=' ')

while (nhiphan!=[]):
    print(nhiphan.pop(),end=' ')



'-----------------------------------------------------------------'

# so_nhi_phan=int(input('Mời bạn nhập số : '))
# print("Binary {0} is {0:b} ".format(so_nhi_phan))
# '''Dùng format để định dạng về số nhị phân'''
 

