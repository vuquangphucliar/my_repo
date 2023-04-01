import mysql.connector

#Get connection
mydb = mysql.connector.connect(
    user='root',
    password='lovecrush',
    host='localhost',
    database = 'mydata'
    
    )
#Query

def need_commit():
    code1 = 'CREATE SCHEMA `test1` ;'
    drop_database = 'drop database `test1` ;'
    drop_table = "DROP table if exists lovecrush"
    delete = "delete from lovecrush where name ='Vu'"
    update_data  = "UPDATE lovecrush set address =%s WHERE address =%s"
    create_table = '''create table lovecrush (id int auto_increment primary key,
                                                name VARCHAR(255),
                                                birth VARCHAR(255),
                                                note VARCHAR(255))'''
    insert = "INSERT INTO lovecrush (name,birth,note) VALUES (%s,%s,%s)"
    code9 = [
        ('Vu','Doan tung 34','khoong cos gif car'),
        ('Nga','Pham kha 34','helllo'),
        ('Phuc','Hai Dương 35','hahahhaha'),
        ('Peter', 'Lowstreet 4','met lamw cow'),
        ('Amy', 'Apple st 652','phiar noox luwcjw'),
        ('Hannah', 'Mountain 21','not give up'),
        ('Michael', 'Valley 345','bo me may'),
        ('Sandy', 'Ocean blvd 2','gia daingh'),
        ('Betty', 'Green Grass 1','nguowig yeu'),
        ]

    '''(id int auto_increment ,
                                                name nvarchar(20) ,
                                                place nvarchar(30),
                                                age varchar(2),
                                                note varchar(10))'''''
    
    #Run
    mycursor = mydb.cursor()
    mycursor.execute("insert into lovecrush (name,place,age,note) values")
    mydb.commit()



def need_fetchall():
    code5 = "show tables"    
    code11 = " SELECT * FROM lovecrush ORDER BY name desc"
    code11 = " SELECT * FROM lovecrush LIMIT 5 OFFSET 2" # start from posittion 3 and return 5 records
    show_databases = "SHOW DATABASES;"

    #Run
    mycursor = mydb.cursor()
    mycursor.execute("select * from lovecrush")
    myresult = mycursor.fetchall()

    for i in myresult:
        print(i)

need_commit()
# need_fetchall()