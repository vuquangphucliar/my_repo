'''Module -- collections'''
from collections import Counter
mylist=[1,5,78,45,4,5,54,5,4,58]
print(Counter(mylist))#Trả về 1 cái đict gồm key là số phần tử không trùng nhau và value là số lần lặp lại của nó
print(Counter(mylist).items())#trả về cx như trên nhưng ở dạng các cặp tuple 
print(Counter(mylist).keys())#trả về mấy cái key
print(Counter(mylist).values())#mấy cái value là số lần lặp lại

'''Module -- itertools'''
mylist='Hack'
from itertools import product,permutations,combinations,combinations_with_replacement
my_repo=(list(product(mylist,repeat=2))) #tạo ra tất cả các list 3 phần tử có khả năng tạo ra từ list hoán vị, lặp lại lấy hết
my_repo=list(permutations(mylist,2))#hoán vị lần lượt 2 ephần tử cho nhau , nhưng vẫn lấy lặp lại phần tử, không loại list trùng phần tử
my_repo=list(combinations(mylist,3))#hoán vị kiểu đơn giản và có lọc các list trùng nhau
my_repo=list(combinations_with_replacement(mylist,2))#cái này với cái product kia na ná nhau không phân biệt đươc
