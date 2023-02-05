def dem_so_chuoi_con():
    while True:
        string_dad=input('Enter your string dad : ').strip()
        if 1<=len(string_dad)<=100:
            string_son=input('Enter your string son : ').strip()
            break
        else:
            print('Try again !')

    i=0;j=0;k=0
    while i<len(string_dad)-len(string_son)  :#     Dùng while để duyệt qua các chuỗi kĩ tư trong strinh
        if string_son == string_dad[i:j+len(string_son)]:#DUyệt qua các chuỗi kĩ tự nhưng là   cụm kí tự 
            # print(string_dad[i:j+len(string_son)]) # 
            k+=1
        i+=1;j+=1

    if k==1 or 0:
        print('The string son appears',k,'time')
    else:
        print('The string son appears',k,'times')
# dem_so_chuoi_con()

def tinn_diem_trung_binh():
    dict1={}
    while True:
        so_luong=int(input('Nhập số lượng học sinh : '))
        if 2<=so_luong<=10:
            break
        else:
            print('Lại !')

    for i in range(so_luong):
        while True:
            name_and_mark=input().split()
            if len(name_and_mark[1::]) ==3:
                name_and_mark1=list(map(lambda x : float(x) , name_and_mark[1::]))
                name_and_mark2 =[i if 0<=i<=100 else 5.0 for i in  name_and_mark1]
                break
            else:print('Try Again !')
        dict1.setdefault(name_and_mark[0],name_and_mark2)
    while True:
        name2=input('Enter your name :')
        if name2 in dict1:
            print(round(sum(dict1[name2])/len(dict1[name2]),2))
            break
        else:
            print('Try again !')

    # print(dict1)
# tinn_diem_trung_binh()
def thay_the_ki_tu():
    string_dad=input('Nhập chuỗi cha :')
    while True:
        string_son=input('Nhập chuỗi con :')
        if string_son in string_dad:
            string_replace=input(f'Bạn muốn thay thế {string_son} bằng gì :')
            string_dad=string_dad.replace(string_son, string_replace)
            print(string_dad)
            break
        else:
            print('Nhập lại đi !')
# thay_the_ki_tu()
def doi_kieu_chu():
    string_dad=input()
    # string_son=input()
    for i in string_dad:
        if i.islower() is True:
            string_dad=string_dad.replace(i,i.upper())
        elif i.isupper() is True:
            string_dad=string_dad.replace(i,i.lower())
    print(string_dad)
# doi_kieu_chu()22


