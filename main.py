from mySQL import *

username = input("Enter your username\n")
password = input("Enter your password\n")
x = checkPasswd(username, password)
if x:
    print("You are logged in!")
    #create a user class with the given username
    session = True
    while session:
        command = input("Enter a command and arguments").split()
        #Create a switch in python, calling one of the class functions inside user.py
        #Perhaps using a dict
        #When logging out, session = False
else:
    print("You've entered invalid credentials, login unsuccesfull.")