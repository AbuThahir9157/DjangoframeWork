# def add():
#     a=int(input("enter"))
#     b=int(input("enter"))
#     print(a+b)
# print("ok")
#
# def sub():
#     a=int(input("enter"))
#     b=int(input("enter"))
#     print(a-b)
# sub()
#
# add()

# def painter(msg):
#     print("message:",msg)
# painter("paint my home")

#
# def findodd(k):
#     if (a%2==0):
#         print('evn')
#     else:
#         print('odd')
#
# a=int(input("enter number"))
# findodd(a)
# def printrange():
#     for i in range (1,20):
#         print(i)
# printrange()

us_name="abu"
up_password="123"
username=input("Enter user Name")
password=input("enter password")

def check():
    if(us_name==username and up_password==password):
        return True
    else:
        return False

a=check()
print(a)