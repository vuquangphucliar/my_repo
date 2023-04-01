# import sys

# try:
#     num=int(input('Nhập 1 số vào đây đi bạn :'))

#     print(num)
# except OSError as err: 
#     print('OS Error : ',err)
# except ValueError:
#     print('Làm sai rồi kìa sửa lại đi !')
# except Exception as err: 
#     print(f"Unexpected {err=}, {type(err)=}")
#     raise

'Câu lệnh thần thánh đưa ra tất cả các exception và 1 số cái builtins trong python'
print('This is all class and module in this file')
[print(i) for i in dir(locals()['__builtins__'])]
[print(i) for i in dir()]
