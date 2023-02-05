def giai_thua(x):
    if ( x == 1 ) or ( x==0):
        return 1
    else:
        return x*giai_thua(x-1)

num=int(input('Mời nhập giá trị x :'))
e_mu=0
for i in range(30):
    e_mu+=num**i/giai_thua(i)
    
sigmoid=e_mu/(e_mu+1)
print(f'Sigmoid_Logistic({num})= {sigmoid}')