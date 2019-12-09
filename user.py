import datetime
from mySQL import *
from prettytable import PrettyTable
from termcolor import colored
class user:
    def __init__(self, uname, mail, perm, scor, groups):
        self.username = uname
        self.email = mail
        self.permissions = perm
        self.score = scor
        self.groups = groups

    def takeShift(self, args): #dateString, movie, group
        if(len(args) != 4):
            print(colored("[-] You have entered the wrong arguments!", "red"))
            print(colored("Format is:\ntakeShift [YYYY-MM-dd] [hh:mm] [movie] [group] ", "red"),colored("Example: takeshift 2019-11-25 08:00 Jumanji Salesperson", "white"))
            return False
        date = datetime.datetime.strptime(args[0]+" "+args[1], "%Y-%m-%d %H:%M")
        movie = args[2]
        group = args[3]
        for i in self.groups:
            if i[0] == group:
                try:
                    addShift(self.username, date, group, movie)
                    print(colored("[+] Successfully added shift!", "green"))
                    return True
                except:
                    print(colored("[-] Failed to add shift, please try again!","red"))
                    return False

    def viewRoster(self): #Roster [Date, Movie_Title, Group, UserID]
        table = PrettyTable(["Date", "Movie Title", "Group", "User ID"])
        for group in self.groups:
            try:
                shows = getShowsForGroup(group)
            except:
                print(colored("[-] Failed to get roster for user: " + self.username,"red"))
                return False
            for show in shows:
                table.add_row(show)
        print(table)

    def cancelShift(self, args): #dato, dato, movie_title, group
        if (len(args) != 4):
            print(colored("[-] You have entered the wrong amount of arguments!", "red"))
            print(colored("Format is:\ncancelShift [YYYY-MM-dd] [HH:mm] [movie] [group] ", "red"),
                  colored("Example: cancelShift 2019-11-25 08:00 Jumanji Salesperson", "white"))
            return False
        date = datetime.datetime.strptime(args[0]+" "+args[1], "%Y-%m-%d %H:%M")
        try:
            cancelShift(self.username, date, args[3], args[2])
            print(colored("[+] You're shift has successfully been cancelled" + str(args[0]+" "+args[1])),"green")
            return True
        except:
            print(colored("[-] Failed to canceled your shift, please try again."),"red")
            return False

    def listUpcommingShows(self, args): #dato, dato
        if (len(args) != 2):
            print(colored("[-] You have entered the wrong arguments!", "red"))
            print(colored("Format is:\nlistUpcomingShows [YYYY-MM-dd] [HH:mm] ", "red"),
                  colored("Example: listUpcomingShows 2019-11-25 08:00", "white"))
            return False
        today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        date = datetime.datetime.strptime(args[0]+" "+args[1], "%Y-%m-%d %H:%M")
        table = PrettyTable(["Date", "Movie Title", "Group", "User ID"])
        shows = getShowsFromDate(today, date)
        for show in shows:
            table.add_row(show)
        print(table)

    def listUnoccupiedShows(self):
        try:
            shows = getShowsForUser("None")
        except:
            print(colored("[-] No unoccupied shows found","red"))
        table = PrettyTable(["Date", "Movie Title", "Group", "User ID"])
        for show in shows:
            table.add_row(show)
        print(colored(table,"yellow"))

    def logOut(self):
        print(colored("[+] Logging out.."),"green")

    def changePassword(self, args):
        if (len(args) != 2):
            print(colored("[-] You have entered the wrong arguments!", "red"))
            print(colored("Format is:\nchangePassowrd [oldPassword] [newPassword]", "red"),
                  colored("Example: changePassword qwerty helloworld", "white"))
            return
        ret = changePassword(self.username, args[0], args[1])
        if ret == False:
            print(colored("[-] Wrong old password entered!", "red"))
            return
        print(colored("[+] Password changed!", "green"))

    def listForShow(self, args): #movie
        if (len(args) != 1):
            print(colored("[-] You have entered the wrong arguments!", "red"))
            print(colored("Format is:\nlistForShow [movie]", "red"),colored("Example: listForShow Jumanji", "white"))
            return False
        shows = getShowsFromTitle(args[0])
        table = PrettyTable(["Date", "Movie Title", "Group", "User ID"])
        for show in shows:
            table.add_row(show)
        print(colored(table,"yellow"))

    def listOfGroups(self):
        print(colored(listGroups(), "yellow"))

    def createGroup(self, args): #new group as arg
        if (len(args) != 1):
            print(colored("[-] You have entered the wrong arguments!", "red"))
            print(colored("Format is:\ncreategroup [group] ", "red"),colored("Example: creategroup cleaner", "white"))
            return
        if createGroup(args[0]) == False:
            print(colored("[-] Failed to add " + args[0] + " as a group","red"))
            return
        print(colored("[+]You've succesfully added " + str(args[0]) + " as a group","green"))

    def addGroup(self, args): #group
        if (len(args) != 1):
            print(colored("[-] You have entered the wrong arguments!", "red"))
            print(colored("Format is:\naddGroup [group] ", "red"),colored("Example: addgroup Salesman","white"))
            return False
        if addGroup(self.username, args[0]) == False:
            print(colored("[-] Failed to add you to the group " + args[0] +"!", "red"))
            return False
        print(colored("[+] You've succesfully added yourself to the group " + args[0],"green"))
        return True

    def listMembersOfGroup(self,args):
        print(colored(listMemberOfGroup(args[0]),"yellow"))
        return True

    def removeGroup(self, args):
        if (len(args) != 1):
            print(colored("[-] You have entered the wrong arguments!", "red"))
            print(colored("Format is:\nremoveGroup [group] ", "red"),colored("Example: removeGroup Salesman","white"))
            return False
        if removeUserFromGroup(self.username, args[0]) == False:
            print(colored("[-] Failed to remove you from the group " + args[0] + "!", "red"))
            return True
        print(colored("[+] You've succesfully removed yourself from the group " + args[0], "green"))
        return False

    def deleteGroup(self, args):
        if (len(args) != 1):
            print(colored("[-] You have entered the wrong arguments!", "red"))
            print(colored("Format is:\ndeleteGroup [group] ", "red"),colored("Example: deleteGroup Salesman","white"))
            return False
        if deleteGroup(args[0]) == False:
            print(colored("[-] Failed to delete the group " + args[0] + "!", "red"))
            return True
        print(colored("[+] You've succesfully deleted the group " + args[0], "green"))
        return False

def listUsers():
    userTable = getUserTable()
    for user in userTable:
        UUID = user[0].decode()
        string = UUID
        for elem in user[1:]:
            string += " " + str(elem)
        print(colored(string,"yellow"))