# import os
# print(os.getcwd())

class Peoples:
    '''Hàm tạo class People'''
    def __init__(self,name='',age='',birthplace='',lover=''):
        self.name=name
        self.age=age
        self.birthplace=birthplace
        self.lover=lover
        # self.all_member=self.take_infos()

def take_info(i=0):
    cv=['Name','Age','BirthPlace']          
    print(f'\vFill in your info textbox below at number {i+1}!')
    sides = [input("\tEnter your "+str(k)+" : ") for k in cv]
    ho_so=Peoples(sides[0],sides[1],sides[2])
    print('\tYour info have been saved !')
    return ho_so

def take_infos():
    sel=int(input('\aHow many people we have ! : '))
    all_people = [take_info(i) for i in range(sel)]
    # print(all_people)
    return all_people
    
def print_all_info(lisst_member):
    for x,y,z in lisst_member:
        print(f'''Your info !
        Name : {x}
        Age : {y}
        Birth Place : {z}''')

def main():
    # ins=Peoples()
    ins=take_infos()
    print_all_info(ins)
main()
            
        

        

        
