def lua_chon():
    x=int(input('''
                        1️⃣ ) 🤣 Hiển thị danh bạ 🤣
                        2️⃣ ) 😍 Thêm liên lạc 😍
                        3️⃣ ) 🤩 Kiểm tra tên liên lạc 🤩 
                        4️⃣ ) 😮 Xóa liên lạc  😮
                        5️⃣ ) 😓 Thoát 😓
                        6️⃣ ) 😥 Xóa danh bạ 😥
                        7️⃣ ) Coming soon

    Enter your choice: '''))
    return x

def show_list():
    with open('Contact.txt','r') as file:
        contacts = file.readlines()
    if not contacts:
        print('Danh bạ trống kìa 🥱')
    else:
        # for i in contacts:
        #     print(i)
        print(*contacts)

def add_contact():
    check=0
    list3=[]
    with open('Contact.txt','r') as file:
        contacts = file.readlines()
    name = input('Nhâp tên😍 :')
    for i in contacts:
        if name in i:
            list3.append(i)
            check = 1
            break
    if check == 1:
        print('Liên lạc đã tồn tại 🥱!')
        print(*list3)
    else:
        number = input('Nhập sdt🤩 : ')
        add_str = f'\t{name:7} : {number}\n'
        file = open('Contact.txt','a')
        file.write(add_str)
        file.close()
        print(f'Đã lưu số {name} 💕')

def check_contact():
    check = False
    lists = []
    with open('Contact.txt','r') as file:
        contacts = file.readlines()
    name1 = input('Tên bạn muốn kiểm tra 🤨 :')
    for i in contacts:
        if i.find(name1) != -1:
            lists.append(i)
            check=True
    if check == True:
        print(f'Tất cả những liên lạc có tên {name1} ')
        print(*lists)
    else:
        print('Tên không tồn tại')
        choice = input(f'Bạn muốn cập nhật luôn số {name1} chứ (y/n) :')
        if choice == 'y':
            add_contact()
        else:
            print('Không thích thì thôi vậy !')

def clear_contact():
    with open('Contact.txt','r') as file:
        contacts = file.readlines()
    while True:
        list2 = []
        name2 = input('Nhập tên liên lạc bạn muốn xóa🫡 :')
        # print(contacts)
        for i in contacts:
            if i.find(name2) != -1:
                list2.append(i)
        if len(list2) == 1:
            break
        else:
           print('\tHãy nhập chính xác tên bạn muộn xóa nhé !')
    print(f'Tạm biệt',*list2,'😢')
    ch = input('Bạn chắc chắn muốn xóa người này chứ (y/n)')
    if ch =='y':
        for i in contacts:
            if i.find(name2) != -1:
                contacts.pop(contacts.index(i))
        with open('Contact.txt','w') as file:
            for i in contacts:
                file.write(i)
    else:
        print('ĐÚng rồi đừng dại mà xóa !')

def clear_all_contact():
    cho = input('Bạn chắc chứ (y/n) :')
    cho2=input('Xóa thật đấy chắc không 😭!')
    if cho2 == 'y':
        with open('Contact.txt','w') as file:
            file.write('')
        print('Rất quyết đoán 😱!')
    else:
        print('Hú hồn 😨!')

def seven():
    pass

def main():
    while True:
        x = lua_chon()
        
        if x == 1:
            show_list()
            
        elif x == 2:
            add_contact()
            while True:
                cho1 = input('Bạn muốn thêm liên lạc khác chứ (Y/n) ')
                if cho1 == 'y':
                    add_contact()
                else:
                    print('Oke Sir !')
                    break
        elif x==3:
            check_contact()
            while True:
                cho1 = input('Bạn muốn check ai nữa không (Y/n) ')
                if cho1 =='y':
                    check_contact()
                else:
                    print('Oke Sir !')
                    break

        elif x==4:
            clear_contact()
            while True:
                cho1 = input('Bạn có muốn xóa thêm đứa nào nữa không (Y/n) ! ')
                if cho1 == 'y':
                    clear_contact()
                else:
                    print('Oke Sir !')
                    break

        elif x==6:
            clear_all_contact()
            
        elif x==5:
            print('Goobye Sir !')
            break 

        else:print('Nhập lại đi pro')
main()