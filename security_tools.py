import random
import string

def validatepassword(userpassword):
    uppercase = 0
    lowercase = 0
    number = 0
    symbol = 0
    space = 0
    #checks if each character is uppercase, lowercase, a number, symbol, space
    for char in userpassword:
        if char.isupper():
            uppercase = uppercase + 1
        elif char.islower():
            lowercase = lowercase + 1
        elif char.isdigit():
            number = number + 1
        elif char.isspace():
            space = space + 1
        elif char == "!" or char == "@" or char == "#" or char == "$" or char == "%":
            symbol = symbol + 1
            #if all good, send back the good words
    if len(userpassword) >= 10 and uppercase >= 1 and lowercase >= 1 and number >= 2 and space == 0 and symbol >= 1:
        ispolicy = True
        return  ispolicy
    else:
        ispolicy = False
        return ispolicy

def validate_ip(address):
    #removes whitespace
    address.strip()
    if "." not in address:
        return False
    #checks if . in ip
    if address.count(".") != 3:
        return False
    parts = address.split(".")
    #checks for 4 numbers 192 168 10 20 
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        #checks if ip follows rule
        number = int(part)
        if number < 0 or number > 255:
            return False
        else:
            return True

def random_password():
    password = ""
    length = random.randint(10,16)
    lett = list(string.ascii_letters)
    num = list(string.digits)
    sym = list(string.punctuation)
    #shuffles list of letters,numbers,symbols so unpredictable and psuedo-random password made
    random.shuffle(lett)
    random.shuffle(num)
    random.shuffle(sym)
    i = 0
    for i in range(length-1):
        char = random.randint(1,3)
        if char == 1:
            password += lett[i]
        elif char== 2:
            r = random.randint(0,9)
            password += num[r]
        elif char == 3:
            password += sym[i]
    return password
random_password()