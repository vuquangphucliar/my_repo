nam=int(input('Nhập số năm bạn muốn :'))
if ( nam % 4 == 0 ):
    if (nam % 100==0):
        if (nam % 400 ==0):
            print('Đây là năm nhuận nha bạn !')
        else:
            print('Đây không phải năm nhuận đâu bạn !')
    else:
        print('Đây là năm nhuận đấy  bạn ')
else:
    print('Đây không phải năm nhuận bạn ơi !')

'------------------------------------------------------------------'

num=int(input("Nhập số năm bạn muốn biết can chi : "))
can=['Canh','Tân','Nhâm','Quý','Giáp','Ất','Bính','Đinh','Mậu','Kì']
chi=[' Thân',' Dậu',' Tuất',' Hợi','Tý',' Sửu',' Dần',' Mão',' Thìn',' Tỵ', 'Ngọ',' Mùi']
print('Năm ',num,'là năm ',can[num%10],chi[num%12])