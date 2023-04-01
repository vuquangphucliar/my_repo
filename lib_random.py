import random

print(random.randint(8,28))#in 1 số nguyên  ngẫu nhiên tử 8 đến 28 và nó không bỏ qua phần tử kết thúc
print(random.random()) # in 1 số thực ngẫu nhiên từ 0 đến 1
print(random.randrange(2,9,2))#in ra 1 số nguyên ngẫu nhiên từ 2 đến 8 và bước nhẩy là 2 


random.seed(6)              # hàm seed này để tạo mầm số ngẫu nhiên
print(random.randint(3,9))  #kết quả của 2 cái này là như nhau vì dùng chung 1 mầm tạo số ngẫu nhiên
print(random.randint(3,9))  #nếu ko tạo mầm thì ct sẽ auto lấy thời gian hiên tại để lm mầm

my_list=['Phúc','Than','Nga','Tú','Vũ']
print(random.choice(my_list))           #Chọn ngẫu nhiên 1 giá trij trong tập hợp dùng choice

random.shuffle(my_list)     #sắp xếp lại các giá trị trong danh sách 1  cách ngẫu nhiên
print(my_list)