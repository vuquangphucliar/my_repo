class Course:
    def __init__(self, name,id_number,lecturer):
        self.name = name
        self.id_number = id_number
        self.lecturer = lecturer
        self.student_list=[]

    def enroll(self,student):
        self.student_list.append(student)

    def print_info(self):
        print(f'Khóa lập trình python cơ bản {self.name} ')
        print(f'Mã Khóa đào tạo {self.id_number}')
        print(f'Lecturer : {self.lecturer}')


class Person():
    def __init__(self,name,age,email) -> None:
        self.name=name
        self.age=age
        self.email=email

    def print_info(self):
        print(f'Cô {self.name} hiện tại {self.age} tuổi !')

class Lecture(Person):
    def __init__(self,name,age,email,bank_account):
        super().__init__(name,age,email)
        self.bank_account=bank_account
    
    def print_info(self):
        print(f'Giáo viên {self.name} hiện tại {self.age} tuổi !')
        print(f'Email: {self.email} ')
        print(f'Bank Account {self.bank_account}')

class Student(Person):
    def __init__(self,name,age,email,student_id):
        super().__init__(name,age,email)
        self.student_id=student_id

    def print_info(self):
        print(f'Học sinh {self.name} hiện tại {self.age} tuổi ')
        print(f"Student id: {self.student_id} and email :{self.email}")


python_course=Course('Lập trình python cơ bản',1234567,'Vũ Quang Phúc')
lecturer_TEK4VN=Lecture('Vũ Quang Phúc',20,'vuquangphuc55gmail.com',379120730)
student_mot=Student('Nguyễn thị Nga',19,'nganguyen@',124221)
student_hai=Student('thannguyen',19,'thannguyen@',124222)
student_ba=Student('anhtan',30,'tanthanh',124223)

python_course.enroll(student_mot)
python_course.enroll(student_hai)
python_course.enroll(student_ba)

python_course.print_info()
lecturer_TEK4VN.print_info()
python_course.print_lit()
