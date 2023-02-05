# def gen(a):
#     'Dùng generator ngốn ít ram hơn comprehension'
#     n=0
#     while n<a: # Nó chỉ trẻ về 1 giá trị tại 1 thời điểm nó được gọi đến
#         yield a # nên dùng 1 điều kiện lặp để nó trả về 1 iterator 
#         a-=1
# # print(sum(gen(5))) 
# def so_le(a):  # hàm tạo ra 1 iterator số lẻ
#     i=0
#     while i<a:
#         yield a
#         a-=2
# def power(lisst): #
#     'Hàm bình phương cái iterator nó nhận vào'
#     for i in lisst:
#         yield i**2
# print(sum(power(so_le(5)))) #generator lòng nhau

# 'dùng except để bắt lỗi stopiterator khi xài cái generator'
# try:
#     ran=int(input('Nhập khoảng giá trị : '))
#     gen=(x for x in range(ran))
#     while True:     # dùng vòng lặp while vô hạn để lặp
#         print(next(gen))
# except StopIteration:
#     print('Hết vòng lặp rồi bạn ơi !')


