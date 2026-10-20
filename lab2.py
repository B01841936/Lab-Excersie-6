#task1
# num1 = int(input("Enter num1 >> "))
# num2 = int(input("Enter num2 >> "))

# print("sum =", num1 + num2)
# print("product =", num1 * num2)
# print("num1 - num2 = ", num1 - num2)
# print("num1 / num2", num1 / num2)
# print("num1 // num2", num1 // num2)
# print("num1 % num2", num1 % num2)
# print("num1 ** num2", num1 ** num2)

#task2
# # inputs:
# hours = int(input("Enter hours gmt"))
# min = int(input("Enter minutes"))
# while min > 59 or min < 0:
#      print("Invalid minutes")
#      min = int(input("Enter minutes"))

# # conversion to time (25 > 01)
# psth = hours + (-8)
# if (psth < 0):
#     psth = 24 + psth
#     if (psth == 24 or psth == 0):
#         psth = "00"
# ceth = hours + 1
# if (ceth > 24):
#     ceth = 0 + 1
#     if (ceth == 24 or ceth == 0):
#             ceth= "00"

# # variables to 24h time format (1 > 01)
# if (psth > 0 and psth < 10 ):
#      psth = "0" + str(psth)
# if (ceth > 0 and ceth < 10 ):
#      ceth = "0" + str(ceth)
# if (min >0 and min <10 ):
#      min = "0" + str(min)

# # display
# print("Time in PST: ", psth, min)
# print("Time in CET: ", ceth, min)

#task3
# eggs = int(input("num of eggs >> "))
# gross = eggs // 144
# dozen = (eggs - (144 * gross)) // 12
# remainder = eggs - ((144 * gross) + (12 * dozen))
# print(eggs, "eggs is", gross, dozen ,remainder)

#task4 
# num = int(input("num between 1 - 100"))
# if(num < 1 or num > 100):
#     print("Invalid Input")
# elif (num % 2) == 0:
#     print("Even number")
# else:
#     print("Odd number")

#task5
# num = int(input("enter number"))
# for counter in range(1, 10 + 1, 1):
#     print(num*counter, end='')

#task6
# password = input("Enter password")
# while password != "password":
#     print("Denied")
#     password = input("Enter password")
# print("Access Granted!")

#task 7
# num1 = 0
# num2 = 1
# for counter in range(1, 20 + 1, 1):
#     next = num1 + num2
#     print(next, end=',')
#     if counter % 2 == 0:
#         num1 = next
#     elif counter % 2 == 1:
#         num2 = next
# or a, b=b, b+a, a = num1, b = num2

#task 8 !!
exit = False
tries = 1
while(exit==False):
    print("1. Security Event Counter")
    print("2. Brute-Force Simulation")
    print("3. Login Authentication")
    print("4. Exit")
    choice = int(input(">> "))
    if (choice < 0 or choice > 4):
        print("Invalid")
        choice = input(">> ")
    elif choice == 4:
        print("Thank you for using the security tool")
        exit = True
    #login
    elif choice == 3:
        exit = True
if choice == 1:
    correct = 0
    false = 0
    password = "password"
    for count in range(10):
        userpass = input("Enter password >> ")
        if userpass == password:
            correct + 1
            print("Correct")
        else:
            false + 1
            print("False")
        percentage = (correct + false) // 100
        if percentage > 50:
            print("Alert! Incorrect password attempts at", percentage,"%")
        else:
            print(percentage,"%")

elif choice == 3:
    user = "user"
    password = "password1"
    username = input("Enter username >> ")
    userpass = input("Enter password >> ")
    while (userpass != password or username != user):
        if tries == 3:
            print("Account frozen for 24h")
        else:
            print("Incorrect details", tries)
            username = input("Enter username >> ")
            userpass = input("Enter password >> ")
            tries + 1
        if userpass == password and username == user:
            print("Authentication Successful")
            break


        


