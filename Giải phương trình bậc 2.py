def giai_nghiem_thuc(a,b,c):
    import math
    căn_delta= math.sqrt(b*b-4*a*c)
    no1= (-b+căn_delta)/2*a
    no2= (-b-căn_delta)/2*a
    print('Nghiệm thứ nhất của phương trình trên là :',round(no1,2))
    print('Nghiệm thứ hai của phương trình trên là :',round(no2,2))
    
def giai_nghiem_kep(a,b):
    no3=-b/2*a
    print('Nghiệm kép của phương trình trên là :',no3)
    
def giai_nghiem_phuc(a,b,c):
    import math
    delta1=-(b*b-4*a*c)
    căn_delta1=math.sqrt(delta1)
    so1=(-b/(2*a))
    so3=2*a
    so2=((căn_delta1)/so3)
    so2=abs(so2)
    print('Nghiệm phức thú nhất là : ',round(so1,3),' + ',round(so2,3),'i',sep='')
    print('Nghiệm phức thứ hai là  : ',round(so1,3),' - ',round(so2,3),'i',sep='')

def main():
    print('Cho phương trình bậc nhất có dạng : Ax+By+C=0')
    a=float(input('Nhập số A: '))
    b=float(input('Nhập số B: '))
    c=float(input('Nhập số C: '))
    delta=b*b-a*c*4
    if (delta>0):
        giai_nghiem_thuc(a,b,c)
    elif(delta==0):
        giai_nghiem_kep(a,b)
    else:
        giai_nghiem_phuc(a,b,c)
main()
