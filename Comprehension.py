# 'Kĩ thuật comprehension với range '
# list_demo=range(30)
# list_using_comprehension=[ i for i in range(30) if i%2==0]# Duyệt các số chia hết cho2 trong khoảng 0-19 vì duyệt nên cần điều kiện if
# print([ i for i in range(20) if i%2!=0 if i % 5==0]) # duyệt 2 câu lệnh if kép
# print(list_using_comprehension)

# 'Kĩ thuật comprehension  ánh xạ'
# list_using_comprehension2=[var **2 for var in range(10) ]# Duyệt các phần tử và bình phương nó lên , Vì nó như 1 dạng ánh xạ 
# print( list_using_comprehension2)  #nên không cần phải đk mà sẽ tác đọng trực tiếp lên các phần tử (khi nó đứng trước for)

# 'Kĩ thuật comprehension dùng hàm để thay đổi giá trị của tất cả các phần tử nó duyệt qua -1 dạng na ná của ánh xạ'
# number = [1.09, 23.56, 57.84, 4.56, 6.78]
# rate = 0.08
#                                                 # Dùng hàm để duyệt qua các phần tử 
# def get_price_with_tax(tax):                    #trong danh sách và cộng với thuế VAT 
#     return tax * (1 + rate)

# final_prices = [get_price_with_tax(i) for i in number] # Dùng hàm để duyệt qua i
# print(sum(final_prices))

# 'Kĩ thuật comprehénsion chuẩn hóa chất lượng nhưung khó hiểu'
# original_prices = [3.12, -2.32, 12.12, 13.14, -6.43] ## Duyệt qua các phần tử số và chuẩn hóa các phần tử lại , nếu lớn hơn 
# prices = [i if i > 0 else 6 for i in original_prices]#không thì oke còn không thì cho bằng không hết , không có âm
# print(prices)# sau if là giá trị nó duyệt , nếu nó oke thì cho qua còn nếu không thì câu sau else kia nó sẽ xuất luôn ra giá trị trả về ( ảo vlinf)

# 'Kĩ thuật comprehension để duyệt kí tự trong dãy ở đây là 1 chuỗi kí tự ở dạng set'
# quote = "Python is easy"
# unique_vowels ={i for i in quote if i in 'aeiou'}
# print(unique_vowels)

# 'Kĩ thuật dùng comprehension với dict , khi dùng với dict thì phải cần thêm key-value ở chỗ 2 chấm kia kìa'
# squares = {i: (i * i) for i in range(10)}  #tạo ra 1 cái đict mà có key là i và value là i bình ư
# print(squares)

# 'Kĩ thuật comprehension với số'
# n=int(input('Nhập số vào đay đi bạn : '))                       #Duyệt tất cả các số trong khoảng n và ion tất cả các số có số 3 
# three = [var for var in range(n) if '3' in str(var) ]  #vì số không sét được cho nên phải ép về kiểu string thì mới xét được
# print(three)

# 'dùng comprehension  để tách chuỗi và loại bỏ kí tự trong chuỗi'
# sentence=input()                                                        #Duyệt qua các phần tử để xem có kí tự nào trùng không 
# result = [var for var in sentence if var not in ['a','e','i','o','u']], #nếu trùng thì trả về khoảng trống ,rồi sau đấy dùng hàm join để nối chuỗi kí tự lại
# print(''.join(result))                                                  #vì nối bằng khoảng trống lên cuối cùng gây ra hiêụ ứng như mình đã xóa kí tự đó


# 'Dùng list comprehension để duyệt qua 2 list khác nhau và cộng các phần tử với nhau để tạo ra 1 danh sachs mới'
# print([x+y for x in ['python','c++'] for y in ['language','programing']])

# Opening the file in read mode and printing the current position of the file pointer.
# with open('mydata.txt','r') as file:
#     print(file.tell())
