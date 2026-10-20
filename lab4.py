
# policy = False
# def validate(userpassword):
#     uppercase = 0
#     lowercase = 0
#     number = 0
#     symbol = 0
#     space = 0
#     for char in userpassword:
#         if char.isupper():
#             uppercase = uppercase + 1
#         elif char.islower():
#             lowercase = lowercase + 1
#         elif char.isdigit():
#             number = number + 1
#         elif char.isspace():
#             space = space + 1
#         elif char == "!" or char == "@" or char == "#" or char == "$" or char == "%":
#             symbol = symbol + 1
#     if len(userpassword) >= 10 and uppercase >= 1 and lowercase >= 1 and number >= 2 and space == 0 and symbol >= 1:
#         ispolicy = True
#         return  ispolicy
#     else:
#         ispolicy = False
#         return ispolicy
        
# while policy == False:
#     password = input("Enter Password >> ")
#     if validate(password) == True:
#         print("Meets Policy")
#         break
#     else:
#         print("Does Not Meet Policy")

#task2

# login = False
# def authenticate(username,password):
#     name = "admin"
#     passwd = "admin123"
#     if username == name and password == passwd:
#         return True
#     else:
#         return False

# while login == False:
#     username = input("Enter Username >> ")
#     password = input("Enter Password >> ")
#     try:
#         if authenticate(username,password) == True:
#             print("Login Successful")
#         else:
#             print("Invalid username or password")
#     except:
#         print("Invalid Input")

#task3

# def calculate_failed_percentage(numfailed,totallogin):
#     failedpercent = (numfailed/totallogin) * 100
#     if failedpercent >= 50:
#         risk = "High Risk"
#     elif failedpercent >=25 and failedpercent < 50:
#         risk = "Medium Risk"
#     elif failedpercent < 25:
#         risk = "Low Risk"
#     failedoutput = str(failedpercent) + "% Failed."
#     return failedoutput,risk

# loop = False
# while loop == False:
#     numfailed = input("Enter Number of Failed Login Attempts >> ")
#     totallogin = input("Enter Total Number of Login Attempts >> ")
#     try:
#         print(calculate_failed_percentage(int(numfailed),int(totallogin)))
#     except ValueError:
#         print("Invalid Input")
#     except ZeroDivisionError:
#         print("Total Logins cannot be 0")

#task4

def validate_ip(address):
    address.strip()
    if "." not in address:
        return False
    if address.count(".") != 3:
        return False
    parts = address.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        number = int(part)
        if number < 0 or number > 255:
            return False
        else:
            return True
    
valid = False
while valid == False:
    address = str(input("Enter IP address >> "))
    if validate_ip(address) == False:
        print("Invalid IP address")
    else:
        break
print("Valid IP address")
    
