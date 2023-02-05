'Closure'

# def set_up(string):
#     'hàm này gọi vào đẻ lấy tham số , hàm to '
    
#     def printf(string2):
#         'còn cái này để closure 1 cái string khác '
#         return string + string2
#         #phải return thì mới dùng được closure
#     return printf

    
# phuc=set_up('Phúc vũ quang')
# phat=set_up('Phat vu quang')

# print(phat(' Hello !'))   # đang dùng chàm losure ,na ná cái object trong class
# print(phuc(phat('Hello 2'))) # cái này cx na ná cái trên chỉ là lồng 2 cái kia thôis

'Decorator'

# def decor1(func):

#     def decorate(string1):
#         print('I just open it first !')
#         func(string1)
#     return decorate

# def decor(func):      #Hàm này sẽ decor cái hàm my_gift hay nói cách khác thì nó là 1 decorator 

#     def decorate(string):                    # xài luôn hàm closure cho máu 
#         print('Your gift have been decorated !')
#         print('And give it to',string)
#         func(string)                        # này mới quan trọng đây ,  thiếu dấu ngoặc thôi là cx ăn lìn rồi

#     return decorate                        # dòng này thì thuộc cái closure kia rồi

# # @decor  # cái dòng này nó tương đưog với cái dòng gán thủ công bên dưới kia , kiểu auto gán decorator  ấy
# @decor1 # 1 hàm có thể được decor bao nhiêu lần cx được, nhưung phải cẩn thạn thứ tự decor, quan trong đấy
# def my_gift(string):                        #hàm này sẽ là hàm bị decor bởi cái hàm bên trên
#     print(' Here is my gift for you, '+string)       

# # my_gift=decor(my_gift)  # dòng này để gán tham chiếu vào chính nó luôn,cú pháp dùng decorator
# my_gift('Vũ Quang Phúc')# dòng này chỉ gọi cái hàm ra  thôi, lúc này là nó đã bị decor rồi


'VÍ DỤ trên tek4 về decorator'
# def star(func):
#     def inner(*args, **kwargs):
#         print("*" * 30)
#         func(*args, **kwargs)
#         print("*" * 30)
#     return inner

# def percent(func):
#     def inner(*args, **kwargs):
#         print("%" * 30)
#         func(*args, **kwargs)
#         print("%" * 30)
#     return inner

# @star
# @percent
# def printer(msg):
#     print(msg)

# printer("Hello")
