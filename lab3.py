# uppercase = 0
# lowercase = 0
# number = 0
# symbol = 0
# password = "Summer2026!"
# #password = input("Enter Password >> ")
# for char in password:
#     if char.isupper():
#         uppercase = uppercase + 1
#     elif char.islower():
#         lowercase = lowercase + 1
#     elif char.isdigit():
#         number = number + 1
#     else:
#         symbol = symbol + 1
# print(len(password),uppercase,lowercase,number,symbol)

#task 2
# uppercase = 0
# lowercase = 0
# number = 0
# symbol = 0
# space = 0
# policy = False
# while policy == False:
#     password = input("Enter Password >> ")
#     for char in password:
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
#     if len(password) >= 10 and uppercase >= 1 and lowercase >= 1 and number >= 2 and space == 0 and symbol >= 1:
#         policy = True
#         break
#     else:
#         policy = False
#         print("Does Not Meet Policy")
# print("Meets Policy")

#task3

# text = "Security Alert: Failed login attempt detected from IP address 192.168.1.25. The user account admin was targeted at 22:45. The server blocked the login attempt after an incorrect password was entered."
# if "Failed" in text:
#     print("Security Event Detected")
# if "login" in text:
#     print("Login Activity Detected")
# position = text.find("192")
# print("IP:", text[position:position + 12])

#task4 
import socket
from datetime import datetime
from random import randint

id = randint(1000,9999)
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip_address = s.getsockname()[0]
s.close()

username = "admin"
password = "adminpass"
usertry = input("Enter Username >> ")
passtry = input("Enter Password >> ")


if usertry == username and passtry == password:
    event = "Successful Login"
else:
    event = "Failed Login"
print(f"ID: {id}\n Username: {usertry}\n IP Address: {ip_address}\n Event: {event}\n Timestamp: {timestamp}")
