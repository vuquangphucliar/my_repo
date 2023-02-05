# import sys

try:
    num=int(input('Nhập 1 số vào đây đi bạn :'))

    print(num)
except OSError as err: 
    print('OS Error : ',err)
except ValueError:
    print('Làm sai rồi kìa sửa lại đi !')
except Exception as err: 
    print(f"Unexpected {err=}, {type(err)=}")
    raise

'Câu lệnh đưa ra tất cả các exception và 1 số cái builtins trong python'
def printf(i):
    print(i)
[printf(i) for i in dir(locals()['__builtins__'])]

'cái này thì đưa ra tất cả các hàm , class ẩn trong 1 file'
def printf(i):
    return i
[print(i) for i in dir()]

phuc=['a',0,6]
for i in phuc:
    try:
        print('the character is',i)
        r=4+i
    except:
        print('lỗi rồi kìa')
print('The result is',r)
