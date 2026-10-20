# ips = ["192.168.10.1","192.168.10.2","192.168.10.3","192.168.10.4","192.168.10.5"]
# print(ips[0],ips[4])
# newip = input("Enter IP >> ")
# ips.append(newip)
# ipremove = input("Enter IP to remove >> ")
# if ipremove in newip:
#     ips.remove(newip)
# print(len(ips))
# iptosearch = input("Enter IP to search >> ")
# if iptosearch in ips:
#     print("In list")
# else:
#     print("Not in list")

#task2

# user = ("bob","192.168.10.1","login","high")
# print(user,len(user))
# if "login" in user:
#      print("In tuple")

#task3

# user = {
#         "username":"bob",
#         "ip":"192.168.10.2",
#         "event":"login",
#         "risk":"high"
#         }
# print(user["username"],user["ip"])
# user["status"] = "blocked"
# user["risk"] = "low"
# del user["event"]
# print(user.keys(),user.values(),user.items())

#task4

# listips = ["192.168.10.1","192.168.10.1","192.168.10.3","192.168.10.4","192.168.10.5"]
# ips = set(listips)
# print(ips)
# newip = input("ip>> ")
# ips.add(newip)
# oldip = input("ip to remove>>")
# ips.remove(oldip)
# iptosearch = input("ip to search>>")
# if iptosearch in ips:
#     print("In list")
# else:
#     print("Not in list")
# print(len(ips))