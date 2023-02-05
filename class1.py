class Info:                                      #class này tạo ra  1 cái info      
    def __init__(self,name,age):               # bao gồm 2 thuộc tính là name và age 
        self.name=name                          #các thuộc tinh này sẽ được lưu lại và được coi là 1 cái ổ chứa
        self.age=age                          #của cái info kia(nó dùng để truy cập cập vào mọi lúc mọi nơi)

def take_info():                                #hàm này lấy dữ liệu 1 l lần và nạp nó 
    Name=input('Enter your name : ')            #vào cái class info kia
    age=input('Enter your age : ')              #rồi return cái info(chính là cái class kia)
    info=Info(Name,age)                         #
    return info

def print_info(info):                           #hàm này nhận vào 1 cái info(chính là cái class bên trên ấy)
    print('Your name : ',info.name)             #rồi print nó ra( khi cho vào đây cái info kia tức là nó
    print('Your age : ',info.age)               #lôi luôn cả cái class vào nên nó có thể sử dụng dữ liệu mà cái class info có

def take_infos():
    total_info=input('Enter how many infos: ')      #hàm này lấy vào nhiều dữu liêu của người dùng
    total_info=int(total_info)                      #chủ yếu nó duyệt cái hàm take inffo bên trên kia
    list_infos=[]                                   #rồi append nó vào 1 cái list
    for i in range(total_info):                     #cái list nó trả lại là list_infos
        print('Number ',i+1)                        #nhưng xuống hàm main lại gán nó bằng in4s
        infor=take_info()                           #đau đầu
        list_infos.append(infor)
    return list_infos

def print_infos(in4s):
    print('-----------')                 #hàm này print ra cái list in4s (cái list mà nãy nó append vào ấy)
    for i in range(len(in4s)):          #
        print_info(in4s[i])             #dòng này ms ảo này(thêm vào cái in4s[i] kiểu nó truyền vào từng phần tử của cái list ấy)

def write_once_info_to_text(info,file):# hàm này để viêt vào file mấy cái kia
    file.write(info.name+'\t')          #chủ yếu để dùng cho cái dưới này
    file.write(info.age+'\n')           #

def write_to_text(in4s):
    with open("lovecrush.txt",'w') as file: # hàm này để chay cái hàm trên cho nó viết vào file 
        file.write(f'{len(in4s)}'+'\n')     #
        for i in range(len(in4s)):              #
            write_once_info_to_text(in4s[i],file)

def read_file_from_txt():
    list_of_info=[]
    with open('lovcrush.txt','r')  as file:#hàm này để đọc từ file 
        total=file.readline()               # file chỉ để lưu data 
        for i in range(int(total)):             #đọc từng dòng 1 rồi lưu vào cái list
            each_info=file.readline()           #
            list_of_info.append(each_info)          #
    return list_of_info
            

 
def main():
    in4s=take_infos() #     gán cái list trả về bên trên kia bằng in4s
    print_infos(in4s)#xuất ra mh in4s
    write_to_text(in4s)# viết vào file qua in4s
main()
