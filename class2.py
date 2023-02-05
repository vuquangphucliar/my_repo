class Student:
    def __init__(self,name,birth,math,liter,eng,classinfo,lover):
        '''hàm khởi tạo class student '''
        self.name=name
        self.birth=birth
        self.math=math
        self.liter=liter
        self.eng=eng
        self.classinfo=classinfo
        self.lover=lover
        self.ave_mark()

    def ave_mark(self):
        '''Hàm tính điểm trung bình các môn học'''
        self.ave=(self.math+self.liter+self.eng)/3
        return self.ave

    def info(self):
        '''Hàm in thông tin của học sinh ra ngoài màn hình'''
        print()
        print(self.name,'là sinh viên lớp',self.classinfo)
        print('Điểm trung bình là',self.ave)
        print('Hiện tại đang crush',self.lover)
        print()
            

def main():
    'Hàm main có vẻ khá cồng kềnh'
    while True:
        name=input('Cho mình xin cái tên đi bạn : ')
        if len(name)  != 0:
            break
        else:
            print('Nhập cẩn thận vào bạn ơi : ')
    while True:
        birth=int(input("Bạn sinh năm bao nhiêu ấy nhờ : "))
        if ( 1900<=birth<=2022 ) :
            break
        else:
            print('Hỏi nốt lần cuối thôi này !')
    while True:
        math=int(input("Toán bạn mấy ấy nhờ : "))
        if ( 0<=math<=10 ):
            break
        else:
            print('Nhập hộ mk cái đi bạn ! ')
    while True:
        liter=int(input("Văn  bạn mấy ấy nhờ : "))
        if ( 0<=liter<=10 ):
            break
        else:
            print('Nhập hộ mk cái đi bạn ! ')
    while True:
        eng=int(input("anh bạn mấy ấy nhờ : "))
        if ( 0<=eng<=10 ):
            break
        else:
            print('Nhập hộ mk cái đi bạn !')
    while True:
        classinfo=input('Bạn học lớp nào đấy : ')
        if len(classinfo)==6:
            break
        else:
            print("Nhập cẩn thận vào nhé bạn !")
    while True:
        lover=input("Người yêu tên gì nói mau : ")
        if lover=='nga':
            break
        else:
            print('Nhập lại đi !')
            
    s1=Student(name,birth,math,liter,eng,classinfo,lover)
    s1.info()
main()