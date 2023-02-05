import random


def way1():
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                        'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']

    SYMBOLS = ['@', '#', '$', '%', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']

    char1=random.choice(DIGITS)
    lowercase_char=random.choice(LOCASE_CHARACTERS)
    uppercase_char=random.choice(UPCASE_CHARACTERS)
    symbol=random.choice(SYMBOLS)

    pass_word=[char1,lowercase_char,uppercase_char,symbol]
    pass_word_char=UPCASE_CHARACTERS+SYMBOLS+LOCASE_CHARACTERS+DIGITS

    length=15
    for i in range(11):
        pass_word.append(random.choice(pass_word_char))

    random.shuffle(pass_word)
    print('Your strong pass word with 15 character:',''.join(pass_word))
def way2():
    """
    It takes a string of all the characters you want to use, and then randomly selects 16 of them to
    make a password
    """
    digits = '1234567890'
    lower_case = "qwertyuiopasdfghjklzxcvbnm"
    upper_case = 'QWERTYUIOPAASDFGHJKLZXZCVBNM'
    symbols = '!@#$%^&*()_+=-|;:,.<>?/[]}{'

    mix = lower_case + upper_case + symbols + digits
    length = 16
    password = "".join(random.sample(mix,length))

    print('Your strong password is:',password)




