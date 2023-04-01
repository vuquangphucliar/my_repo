import pymongo
    

def choice():
    choice = input('''                      OPTION to you 
            1)insert data           2) find
            3)sort                  4)delete
            5)update                6)Exit()
                
    Enter your choice :''')
    return choice

print('\n\aWELCOME to my database !')
while True:
    key = input('Enter your localhost: ')
    if key == '27017':
        print('ACCESS LOCALHOST:27017 ! lovecrush')
        myclient = pymongo.MongoClient(f'mongodb://localhost:{key}/')
        mydb = myclient[input("admin")]
        mytable = mydb[input('Your table: ')]
        print("fYou're working on Databases//admin//my_data2\n")
        break

def dict1(i): 
    '''Return the dict to take arguement cho cái list dưới kia'''
    print('\aThe Doc',i+1)
    return {'_id':input('Enter your ID: '),
            'name':input('Enter your name: '),
            'address':input('Enter your address: ')}

def insert():
    '''take dict of list to be an argument for (insert_many)'''
    ran = int(input('How many doc you want to insert in this table :'))
    list1 = [dict1(i) for i in range(ran)]
    mytable.insert_many(list1)

def findd():
    list2 = "_id name address".split()
    choice = input(f"You want to show '{list2[0]}' or '{list2[1]}' or '{list2[2]}:' ")
    if  choice.lower() == "name": 
        for i in mytable.find({},{'name':1,'_id':0}):
            print(i)
    elif  choice.lower() == "address":
        for k in mytable.find({},{'address':1,'_id':0}):
            print(k)
    elif  choice.lower() == '_id':
        for l in mytable.find({},{"_id":1}):
            print(l)
    elif choice =='':
        for j in mytable.find():
            print(j)
    else:print('\a\tcó nhập thôi cx không thành hồn !')
    # for i in mytable.find({},{choice:1}):
    #     print(i)
    
def delete_():
    if input('DO you want to delete a table or a database: ') == "table":
        mytable.delete_many({})
    else:
        check = input('''This'll make your database be gone forever\n 
    Are you sure (y/n)!  ''')
        if check == 'y':
            mytable.drop()

    

    # choice2 = input('You want to delete this table (y/n)')
    # if choice2 == 'y':

# insert()
# choice()    
delete_()


