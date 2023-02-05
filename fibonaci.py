# def fibonaci_of_n(n):
#     f0=0
#     f1=1
#     for i in range(n):
#         f2=f1+f0
#         f1=f2
#         f0=f1
#     return f2/f1
# def main():
#     n = int(input("Enter n: "))
#     print('The Golden Rate =',fibonaci_of_n(n))
# main()

' fibonaci dùng kĩ thuật unpacking'
def fib(n):
    n=int(input('Nhập số lượng số fibonaci bạn muốn xem :'))
    a, b = 1, 1
    print(0, end=' ')
    for i in range(n):
        a, b = b, a + b
        print(a,end=' ')
fib(n)