import datetime

'''module -- datetime.date'''
# print('Date and time today:',datetime.date.today())# in năm-tháng-ngày hiện tại
# # [print(i) for i in dir(datetime)]# tất cả các class trong datetime
# print('Datetime was modified:',datetime.date(2004,10,16))       # Modify datetime
# 'Cách lấy ngày tháng năm đơn giản'
# today = datetime.date.today()
# print('Current Year',today.year)
# print('Current day',today.day)
# print('Current month',today.month)
# print('Date format by timestamp:',datetime.datetime.fromtimestamp(1673920054))#huyển đổi từ UNix time xang giời ngày tháng, type datetime.date
# print(type(datetime.datetime.fromtimestamp(1673920054))) # cái type phụ thuộc vào xài class gì: datetime hay date trong cái module datetime


'''Module -- datetime.time'''
'''Không có j chú ý lắm'''
# a= datetime.time
# print(a) # không ghi gì nó sẽ hiểu là 00:00:00
# b=datetime.time(8,59,45) #1 cách để chỉnh giờ phút giây 
# c=datetime.time(hour=8,minute=59,second=46)# bản đầy đủ như này
# d=datetime.time(8,45,59,455353)# bản bonus thêm microsecond
# print(b,'\n',c,'\n',d)


'''Module -- datetime.datetime'''
# print(datetime.datetime(2023,1,17,9,50,45,434433)) # full argument edited
# print(datetime.datetime.now()) # full real time
# print(datetime.datetime.now().year)   
# print(datetime.datetime.now().month)
# print(datetime.datetime.now().day)
# print(datetime.datetime.now().hour)
# print(datetime.datetime.now().minute)
# print(datetime.datetime.now().second)
# print(datetime.datetime.now().microsecond)
# print(datetime.datetime.now().timestamp()) # lấy micro timestamp hiện tại 


'''Module -- datetime.timedelta'''
# ''' dùng toán tử để lấy sự chênh lệch'''
# birthday=datetime.datetime(2004,10,16,9,30,34,121212)
# today=datetime.datetime.now()
# print(birthday,'\n',today) # checks
# age=today-birthday    # dùng dấu - để tính ngày chênh lệch
# print(age)   # dùng dấu - thì không cần ép về kiểu timedelta
# print(type(age))
# print(age.total_seconds()) # lấy giây chênh lệch
# day1=datetime.timedelta(3,0,0,0,45,0,0)  # Muốn dùng toán tử khác thì phải ép về timedelta
# day2=datetime.timedelta(4,0,0,0,34,2,0) # phải ép về timedelta
# print(day1+day2)  #  không nó không cho xài đâu


'''strftime'''
'Xuất type datetime ra string dùng strftime nghi nó là string format time'
# now=datetime.datetime.now()
# print('Month1 now : '+now.strftime('%h' ),now.strftime('%b'),now.strftime('%B')) # in ra tháng hiện tại bằng tiếng anh
# print('Time now tpye 24 hour: '+now.strftime('%H:%M:%S %p'),'or type 12 hour:',now.strftime('%I:%M:%S %p')) # đây là khuôn rồi cứ thế dập thôi
# print('Day now : '+now.strftime('%d/%m/%Y') +' or another type day :'+ now.strftime('%d/%m/%y'))  # Có chữ y hoa thôi cx là cả vấn đề đấy
# print('Name day in week: '+now.strftime('%a')+' or '+now.strftime('%A'))
# print('Day in week From 0 to 6 :',now.strftime('%w')) # KNó bắt đầu từ chủ nhật chứ không phải thứ 2 đâu
# print('Micro second now:',now.strftime('%f')) # lấy microsec 6 số
# print('Day in year:',now.strftime('%j')) # Từ 1 đến 365
# print(now.strftime('%c')) #  format xang thứ tháng ngày giờ năm
# print('Only time:',now.strftime('%X'),'and day:', now.strftime('%x')) # lấy giờ nhanh , nhưng còn cái ngày ở dạng mm/dd/yy chán luôn


'''strptime'''
'''Đối lại với cái strftime'''
# string_date = input('Enter by type (dd/mm/yy): ')
# strftime= datetime.datetime.strptime(string_date,'%d/%m/%y')
# print(strftime)
#Không hiểu format kiểu j nó cứ bị ngược

'''module -- pytz '''
'''Lấy timezone ở 1 địa điểm khác'''
# import pytz
# local = datetime.datetime.now()  #lấy time hiện tại
# print('Local time is '+local.strftime('%d/%m/%Y'))#    str  Format time
# tz = input('Enter your timezone: ') # nhập gần đúng cx được , nó sẽ check trong cái timezone, na ná nhau vào
# timezone_newyork=pytz.timezone(tz)#   lấy tên múi giờ cho cái hàm now() nó check giờ
# print('Time Zone:',timezone_newyork)# Cái múi giờ dùng module pytz lấy sẽ ổn hơn
# tz_NY = datetime.datetime.now(timezone_newyork)   # Trả về múi giờ để tí format trang string, vì nó ko phải string, nó thuộc cái class tztime
# str_tz_NY = tz_NY.strftime('%d/%m/%y, %H:%M:%S')#   Format xang string Có thể lm ngay bước trên nhưng lm ở đây cho đỡ rối
# print("Time in your timezone now: ",str_tz_NY)
# [print(i) for i in pytz.all_timezones] # Xuẩt tất cả các múi h có trong cái module pytz


import time
# print('Before sleep')
# # time.sleep(2.9)
# print('After sleep')
# epoch=time.time()   # lấy timestsmp hiện tại chuẩn đến 6 chữ số
# print(epoch)
# print(time.ctime(epoch)) # na ná cái fromtimestamp cx kiểu dịch cái timestamp ra
# # print(datetime.datetime.fromtimestamp(epoch))
# print(now.strftime('%c'))
# print(time.localtime()) #Xuất ra cái time.struct_time
# print(time.localtime(1671610080).tm_year) # dùng cái struct_time kia để truy cập vào year
# print(time.gmtime())   # lấy h theo chuẩn quốc tế UTC
# local = time.localtime()
# print(time.mktime(local)) # mktime dịch cái time.struct về timestamp 
# print(time.asctime(local)) # vẫn dịch struct_time nhưng về dạng khác 



def clock_now():
    """
    Clock() prints the current time in the format HH:MM:SS, and then erases it and prints the current
    time again, and so on, forever
    """
    '''Đồng hồ đếm giờ hiện tại 🤧
    Dùng while lặp vô tận time now sau mỗi 1s
    THuật toán cả '''
    while True:
        now=datetime.datetime.now()  # Lấy thông tin time now
        print('\t',now.strftime('%X'),end='\r')   # 2  dòng print này có giá trị nhất trong cái vòng lặp này
        # print("\rHiHi", end="") # dòng này mới là sự kích thích '\r'
        time.sleep(1)
# clock_now()

def take_secs(func):

    def inner():    
        sec = int(input('Enter your Secs: '))
        func(sec)

    return inner

@take_secs
def countdown(t):
    '''Đồng hồ đếm ngược style AI code
    Không cần lấy time now mới chất chứ
    Dùng vòng lặp while để lấy số lần lặp và cx dùng nó để xuẩt ra số phút số giây luôn, 😱
    THuật toán: lấy số giây nhập từ bàn phím rồi dùng hàm divmode để chia lấy số dư 
    Click on the func to see more detail
    COi thương là phút còn số dư là giây, GẮT
    THích chơi format'''
    while t:                 # Kiểu dùng while False này để duyệt số lần lặp đúng là xịn thật
        mins, secs = divmod(t, 60)          # dùn hàm để trả về 1 tuple ,Tự xem đi
        hours, minss =divmod(mins, 60 )     
        # timeformat = '{:02d}:{:02d}'.format(mins, secs) # Cách con AI nó format 
        timeformat = f'\t{hours:>02}:{minss:>02}:{secs:>02}'
        print(timeformat, end='\r')   # Cái đoạn cuối nó là cả vấn đè đấy
        time.sleep(1)  # Cho nó ngủ one secs
        t -= 1 
    print('\tTime Out !\n')

countdown()


def timer_basic(t=1):
    """
    It takes a time in seconds as an argument, and prints a timer_basic in the format of
    hours:minutes:seconds, counting up from the time given
    
    :param t: The time in seconds to count up from, defaults to 1 (optional)
    """
    import time as tm
    check = input('''\tWELCOME to my timer ! 
        Press Enter To continue: ''')
    while t:
        a = datetime.datetime.fromtimestamp(t)
        time = a.strftime(f'\t{t//3600:>02}:%M:%S')
        print(time,end='\r')
        tm.sleep(1)
        # Incrementing the value of t by 1.
        t+=1
        
# timer_basic()