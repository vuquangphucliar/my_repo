items={1,2,3,4,5,8,9,12,15,17,21,25,27,31,32,38,40,44,48,50}
n=int(input('Nhập số dòng đi bạn : '))
lines=[]
for i in range(n):
    line=input('Get_items : ').split(' ')
    lines+=line
# print(lines)
lines = set(map(lambda x: int(x) , lines))
# print(lines)
# print(items.intersection(lines))
giao=items&lines
if len(giao)/len(lines)>0.4:
    print('YES')
else:
    print('NO')