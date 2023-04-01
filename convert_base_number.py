def bin_to_dec():
    '''convert a binary number to a decimal number'''
    num = "0b"+input("Enter your binary number: ")
    # print(f"COnvert binary {num} to dedimal base: {num:d}")
    # print(f"binary {10} to decimal {0b100000000:d}")
    print(f"Convert Binary base {num} to decimal base",int(num,0))
def bin_to_hex():
    '''convert a binary number to hexa number '''
    num ="0b"+input("Enter your binary number: ")
    print("Convert binary base {num} to hexa base ",end='')
    num = int(num,0)
    print(f"{num:X}")
def dec_to_bin():
    '''convert a decimal number to binary number'''
    num = int(input("Enter your decimal number: "))
    # print("Convert decimal base" ,num, "to binary base: {0:b}".format(num))
    print("Convert decimal base" ,num, "to binary base:",bin(num))
def dec_to_hex():
    '''convert a decimal number to hexadecimal number '''
    num = int(input("Enter your decimal number: "))
    # print("Convert decimal base" ,num, "to hexa base: {0:X}".format(num))
    print("Convert decimal base" ,num, "to hexa base:",hex(num))
def hex_to_bin():
    '''convert a hexa number to binary number'''
    tup_hex = ("0 1 2 3 4 5 6 7 8 9 a b c d e f").split(' ')
    tup_bin = ("0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111").split(" ")
    num = input("Enter your hex number (lower case): ") 
    print(f"Convert hexa base {num} to binany base",end=" ")  
    for i in num:
        print("".join(tup_bin[tup_hex.index(i)]),end=" ")
def hex_to_dec():
    '''convert a hexa number to decimal number '''
    tup_hex = ("0 1 2 3 4 5 6 7 8 9 a b c d e f").split(' ')
    tup_bin = ("0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111").split(" ")
    bin_case = "0b"
    num = input("Enter your hex number (lower case): ")
    for i in num:
        bin_case += "".join(tup_bin[tup_hex.index(i)])
    # print(bin_case)
    print(f"Convert hexa base {num} to decimal base:",int(bin_case,0))
def continue_(func):
    '''this is my docstring for this function to check if you wanna continue your choice'''
    while True:
        if input("\tContinue...(y/n): ") == "y":
            func()
        else:break
def check():
    '''return a check for my choice in function below'''
    return input('''
    \t  1,BIN to dec\t 3,DEC to bin\t5,HEX to bin\t7,exit
    \t  2,BIN to hex\t 4,DEC to hex\t6,HEX to dec\n
    \tWhat do you want: ''' )
def main():
    """This fuction will create a menu for these funcion above and use it to perform Convert"""
    print("\t\tWelcome to my Convert base 😁😁😁\n\tHello, Sir !")
    while True:
        chose = check()
        if chose == "1":
            bin_to_dec()
            continue_(bin_to_dec)
        elif chose == "2":
            bin_to_hex()
            continue_(bin_to_hex)
        elif chose == "3":
            dec_to_bin()
            continue_(dec_to_bin)
        elif chose == "4":
            dec_to_hex()
            continue_(dec_to_hex)
        elif chose == "5":
            hex_to_bin()
            continue_(hex_to_bin)
        elif chose == "6":
            hex_to_dec()
            continue_(hex_to_dec)
        elif chose == "7":
            print("Goodbye, SIR !")
            break
        else:print("Try again !")
main()
