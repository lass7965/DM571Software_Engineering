from mySQL import *
from user import *

def listUsers():
    userTable = getUserTable()
    for user in userTable:
        UUID = user[0].decode()
        string = UUID
        for elem in user[1:]:
            string += " " + str(elem)
        print(string)


datetime.datetime(2019, 11, 21, 22, 0)


def main():
    username = input("Enter your username\n")
    password = input("Enter your password\n")
    x = checkPasswd(username, password)
    if x:
        print("You are logged in!")
    # create a user class with the given username
        userTable = getUser(username)  # [UUID, Username, Email, Permission, Score, Groups]
        currentuser = user(username, password, userTable[2], userTable[3], userTable[4], getGroups(username))
        session = True
        while session:
            command = input("Enter a command and arguments").split()
            if command == "takeShift":
                currentuser.takeShift("2019-11-21 13:31:00")
            elif command == "viewRoster":
                currentuser.viewRoster()
            elif command == "cancelShift":
                currentuser.cancelShift("2019-11-21 13:31:00")
            elif command == "listUpcommingShows":
                currentuser.listUpcommingShows()
            elif command == "listUnoccupiedShows":
                currentuser.listUnoccupiedShows()
            elif command == "logOut" or "q":
                currentuser.logOut()
                session = False
            elif command == "changePassword":
                currentuser.changePassword("xXxXxX")
            elif command == "listUsers":
                listUsers()
            elif command == "fetchListForGivenShow":
                currentuser.fetchListForGivenShow()
            elif command == "listGroups":
                currentuser.listGroups()
            elif command == "createGroup":
                currentuser.createGroup()
            elif command == "addUserToGroup":
                currentuser.addUserToGroup()
            elif command == "listMembersOfGroup":
                currentuser.listMembersOfGroup()

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