from user import *

def printHelp():
    print(colored("listUsers ","white",attrs=["bold"]),colored("\nLists all the registered users of the application","white"),colored("\nExample: listUsers\n","grey"))
    print(colored("takeShift [YYYY-MM-dd] [hh:mm] [movie] [group]", "white", attrs=["bold"]),
          colored("\nEnlist a shift", "white"),
          colored("\nExample: takeshift 2019-11-25 08:00 Jumanji Salesperson\n", "grey"))
    print(colored("viewRoster", "white", attrs=["bold"]),
          colored("\nView all shifts for the groups you have assigned youself to\n", "white"))
    print(colored("listUpcomingShows [YYYY-MM-dd] [hh:mm]", "white", attrs=["bold"]),
          colored("\nList all shows scheduled to be run from today until a given date", "white"),
          colored("\nExample: listUpcomingShows 2019-11-25 08:00\n", "grey"))
    print(colored("addGroup [group]", "white", attrs=["bold"]),
          colored("\nAssign yourself to a given group", "white"),
          colored("\nExample: addGroup salesperson\n", "grey"))
    print(colored("removeGroup [group]", "white", attrs=["bold"]),
          colored("\nRemove yourself to a given group", "white"),
          colored("\nExample: removeGroup salesperson\n", "grey"))
    print(colored("listUnoccupiedShows", "white", attrs=["bold"]),
          colored("\nView all unoccupied shifts you can assigned youself to\n", "white"))
    print(colored("listForShow [movie]", "white", attrs=["bold"]),
          colored("\nList all shifts for a given show", "white"),
          colored("\nExample: listForShow Jumanji\n", "grey"))
    print(colored("changePassword [oldPassword] [newPassword]", "white", attrs=["bold"]),
          colored("\nChange your password into something new", "white"),
          colored("\nExample: changePassword qwerty helloworld\n", "grey"))




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
                currentuser.viewRoster()
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
            elif command[0].lower() == "listforshow":
                currentuser.listForShow(command[1:])
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
                printHelp()
            else:
                print(colored("Unknown command. Type 'help' if you need a list of commands"))
    else:
        print("You've entered invalid credentials, login unsuccesfull.")
        return

while (True):
    createOrLogin = input("Press y to login, press n to create user\n")
    if createOrLogin.lower() == "y":
        main()
        break
    elif createOrLogin.lower() == "n":
        username = input("Please enter a username\n")
        password = input("Please enter your password\n")
        email = input("Enter a email please\n")
        createUser(username,password,email,1)
        break