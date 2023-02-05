square= lambda x: x ** 2
lap_phuong= lambda x: x **3
n=int(input('Nhập 1 số vào đây : '))
print('Bình Phương Của N =',square(n))
print('Lập phương của n =',lap_phuong(n))


first_name=input('Nhập tên của bạn : ')
last_name=input('Nhập họ của bạn : ')
full_nmae=lambda first_name,last_name:print(f'{last_name} {first_name}')
full_nmae(first_name,last_name)

my_list=[]
s=1
print('Nạp số vào list đi bạn')
while True:
    print('Số thứ',s,':',end='')
    n=int(input())
    s+=1
    if n==0:
        break
    my_list.append(n)
print(my_list) # Nạp số vào list 

my_list1=list(filter(lambda x : (x%2 == 0) , my_list))
print(my_list1)         #DÙng hàm filter để lọc số chẵn, ảo phết

my_list2=list(map(lambda x : x*2 , my_list1))
print(my_list2)         #dùng hàm map để nhân tất cả các phần tử trong list kia với 2
# nó là ánh xạ đấy , ánh xạ f đi từ my_list1 xang my_list 2 đấy

