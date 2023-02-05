def prime(num):
    num=int(num)
    k=0
    for i in range(1,int(num)+1):
        if num % i == 0:
            k+=1
    if k == 2:
        return num

def se_pa(num):
    num=str(num)
    k=0;n=0
    while k < len(num):
        if num[0:k] != '':
            if prime(num[0:k]) == None: 
                n+=1
        k+=1
    if n == 0:
        return num

def super_prime(num):
    def inner():
        if prime(num) != None:
            if se_pa(num) != None:
                print(num,'is a super prime')

    return inner()
def main():
    """
    It takes a number, and if it's a super prime, it prints it
    """
    k=50
    while k:
        super_prime(k)
        k-=1
main()