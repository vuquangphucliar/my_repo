def tính_tiền_thừa(tổng_số_tiền_táo,số_tiền_bạn_đưa):
    if số_tiền_bạn_đưa < tổng_số_tiền_táo:
        return -1
    else:
        return số_tiền_bạn_đưa - tổng_số_tiền_táo

def tính_tiền_táo(số_cân_táo,số_tiền1cân_táo):
    return số_cân_táo * số_tiền1cân_táo

def xử_lý_tiền_thừa(tong):
    tờ500=int(tong/500)
    tong=tong-tờ500*500
    if tờ500!=0:
        print('Số tờ 500 là : '+str(int(tờ500)))
    
    tờ200=int(tong/200)
    tong=tong-tờ200*200
    if tờ200 !=0:
        print('Số tờ 200 là: '+str(int(tờ200)))
    
    tờ100=int(tong/100)
    tong=tong-tờ100*100
    if tờ100!=0:
        print('Số tờ 100 là : '+str(int(tờ100)))
    
    tờ50=int(tong/50)
    tong=tong-tờ50*50
    if tờ50!=0:
        print('Số tờ 50 là : '+str(int(tờ50)))

    tờ20=int(tong/20)
    tong=tong-tờ20*20
    if tờ20!=0:
        print('Số tờ 20k là : ',int(tờ20))
    
    tờ1k=int(tong/1)
    print('Số tờ 1 nghinf là: '+str(int(tờ1k)))

def tien_con_thieu(tổng_số_tiền_táo,số_tiền_bạn_đưa):
    return tổng_số_tiền_táo-số_tiền_bạn_đưa
    
def main():
    số_tiền1cân_táo=20
    số_cân_táo=float(input('Nhập số cân táo bạn mua(20k/kg) : '))
    số_tiền_bạn_đưa=float(input('vui lòng thanh toán(k-VND) :'))
    
    
    tổng_số_tiền_táo=tính_tiền_táo(số_cân_táo,số_tiền1cân_táo)
    số_tiền_trả_lại=tính_tiền_thừa(tổng_số_tiền_táo,số_tiền_bạn_đưa)
    tien_thieu=tien_con_thieu(tổng_số_tiền_táo,số_tiền_bạn_đưa)
    print('Tổng số tiền táo  là :'+ str(tổng_số_tiền_táo))
    if số_tiền_trả_lại==-1:
        print(f'Thiếu {tien_thieu} nghìn !')

    else:
        print('Số tiền phải trả lại là :'+str(số_tiền_trả_lại))
        
        xử_lý_tiền_thừa(số_tiền_trả_lại)
                                                                    
main()
