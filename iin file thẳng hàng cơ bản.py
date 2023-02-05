import pandas as pd
dic6={"Name":[],"Age":[],"Class":[]};I=[]#
while 1:#
    name=input('Enter your name : ')#       Lấy dữ liệu đầu vào
    if ( name =='' ):#
        break                                  
    age = input('Fill your age : ')     
    classs=input('Fill your class : ')
    dic6['Name'].append(name)#          truy xuất vào cái list qua cái tên keys
    dic6['Age'].append(age)#            
    dic6['Class'].append(classs)#
    
Class_DataFrame=pd.DataFrame(dic6)#             cho cái list thành dạng data frame (khung dũw liệu)
for i in range(1,len(dic6['Name'])+1):#         |cái này để cho in dex của mấy cái dòng start at 1
    I.append(i)#                                |
Class_DataFrame.index=I#                        |
with open('mydata.txt','w',encoding='utf-16') as file:# |Thao tác mở và ghhi vào file text
    file.write(str(Class_DataFrame))#                   |phải đưa cái data frame về text thì ms ghi được

with open('mydata.txt','r',encoding='utf-16') as file:# |Đọc file (cái utf 16 kia để ghi text có đấud)
    hehe=file.read()#                                   |đọc tất cả cái gì có trong file
    print('List Students !\n')
    print(hehe)
# cách đọc file thứ 2
# with open('mydata.txt','r',encoding='utf-16') as file:
#     for i in file.readlines():
#         print(i)