from user import *
def loginTest(username, password):
    if checkPasswd(username,password):
        print("You are logged in!")
        userTable = getUser(username)
        currentuser = user(username, userTable[2], userTable[3], userTable[4], getGroup(username))
        #Do testing commands

        #Done testing commands
        print("Testing complete!")

def createLoginTest(username,password,email):
    createUser(username,password,email,1)
    loginTest(username,password)