#brings other files functions
import security_tools
#inputs
password = input("Enter Password >> ")
ipaddress = input("Enter IP >>")
#if results of function == false, tell user
if security_tools.validatepassword(password) == False:
    print("Suggested Password: ",security_tools.random_password())
if security_tools.validate_ip(ipaddress) == False:
    print("Invalid IP")