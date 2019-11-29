from user import *

def listUsers():
    userTable = getUserTable()
    for user in userTable:
        UUID = user[0].decode()
        string = UUID
        for elem in user[1:]:
            string += " " + str(elem)
        print(string)

def main():
    username = input("Enter your username\n")
    password = input("Enter your password\n")
    x = checkPasswd(username, password)
    if x:
        print("You are logged in!")
    # create a user class with the given username
        userTable = getUser(username)  # [UUID, Username, Email, Permission, Score, Groups]
        currentuser = user(username, userTable[2], userTable[3], userTable[4], getGroup(username))
        session = True
        while session:
            command = input("Enter a command and arguments\n").split()
            if command[0].lower() == "takeshift":
                currentuser.takeShift(command[1:])
            elif command[0].lower() == "viewroster":
                currentuser.viewRoster(command[1:])
            elif command[0].lower() == "cancelshift":
                currentuser.cancelShift(command[1:])
            elif command[0].lower() == "listupcomingshows":
                currentuser.listUpcommingShows(command[1:])
            elif command[0].lower() == "listunoccupiedshows":
                currentuser.listUnoccupiedShows()
            elif command[0].lower() == "changepassword":
                currentuser.changePassword(command[1:])
            elif command[0].lower() == "listusers":
                listUsers()
            elif command[0].lower() == "fetchlistforgivenshow":
                currentuser.fetchListForGivenShow(command[1:])
            elif command[0].lower() == "listgroups":
                currentuser.listOfGroups()
            elif command[0].lower() == "creategroup":
                currentuser.createGroup(command[1:])
            elif command[0].lower() == "deletegroup":
                currentuser.deleteGroup(command[1:])
            elif command[0].lower() == "addgroup":
                currentuser.addGroup(command[1:])
            elif command[0].lower() == "removegroup":
                currentuser.removeGroup(command[1:])
            elif command[0].lower() == "listmembersofgroup":
                currentuser.listMembersOfGroup(command[1:])
            elif command[0].lower() == "logout" or command[0].lower() ==  "q":
                currentuser.logOut()
                session = False
            elif command[0].lower() == 'help' or command[0].lower() == "?":
                print("Can't help you! You are on your own!")
                continue ####Help message not implemented, should list all usercommands and usage
            else:
                print(colored("Unknown command. Type 'help' if you need a list of commands"))
# Create a switch in python, calling one of the class functions inside user.py
# Perhaps using a dict
# When logging out, session = False
    else:
        print("You've entered invalid credentials, login unsuccesfull.")
        return

while (True):
    createOrLogin = input("Press y to login, press n to create user\n")
    if createOrLogin.lower() == "y":
        main()
        break
    elif createOrLogin.lower() == "n":
        createUser()
        break