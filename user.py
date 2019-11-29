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
            print(colored("[-] Format is:\ntakeShift %date %movie %group ", "red"),colored("Example: takeshift 2019-11-25 08:00 Jumanji Salesperson", "white"))
            return False
        date = datetime.datetime.strptime(args[0]+" "+args[1], "%Y-%m-%d %H:%M")
        movie = args[2]
        group = args[3]
        for i in self.groups:
            if i[0] == group:
                ret = addShift(self.username, date, group, movie)
                if(ret == True):
                    print(colored("[+] Successfully added shift!", "green"))
                    break
                print(colored("[-] Failed to add shift, please try again!","red"))
                break

    def viewRoster(self, args): #Roster [Date, Movie_Title, Group, UserID]
        if (len(args) != 0):
            print(colored("[-] You have entered the wrong arguments!", "red"))
            print(colored("[-] Format is:\ntakeShift %date %movie %group ", "red"),
                  colored("Example: takeshift 2019-11-25 08:00 Jumanji Salesperson", "white"))
            return False
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        shows = getShowsForUser(self.username)
        table = PrettyTable(["Date", "Movie Title", "Group", "User ID"])
        for show in shows:
            table.add_row(show)
        print(table)

    def cancelShift(self, args): #dato, dato, movie_title, group
        if (len(args) != 4):
            print(colored("[-] You have entered the wrong arguments!", "red"))
            print(colored("[-] Format is:\ntakeShift %date %movie %group ", "red"),
                  colored("Example: takeshift 2019-11-25 08:00 Jumanji Salesperson", "white"))#######Har ikke lavet et eksempel endnu
            return False
        date = datetime.datetime.strptime(args[0]+" "+args[1], "%Y-%m-%d %H:%M")
        temp = cancelShift(self.username, date, args[3], args[2])
        if temp == True:
            print("[+] You've succesfully canceled your shift on" + str(args[0]+" "+args[1]))
        else:
            print("[-] You've unsuccesfully canceled your shift, please try again.")

    def listUpcommingShows(self, args): #dato, dato
        if (len(args) != 2):
            print(colored("[-] You have entered the wrong arguments!", "red"))
            print(colored("[-] Format is:\ntakeShift %date %movie %group ", "red"),
                  colored("Example: takeshift 2019-11-25 08:00 Jumanji Salesperson", "white"))#######Har ikke lavet et eksempel endnu
            return False
        today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        date = datetime.datetime.strptime(args[0]+" "+args[1], "%Y-%m-%d %H:%M")
        table = PrettyTable(["Date", "Movie Title", "Group", "User ID"])
        shows = getShowsFromDate(today, date)
        for show in shows:
            table.add_row(show)
        print(table)

    def listUnoccupiedShows(self):
        shows = getShowsForUser("None")
        table = PrettyTable(["Date", "Movie Title", "Group", "User ID"])
        for show in shows:
            table.add_row(show)
        print(table)

    def logOut(self):
        print("[+] Logging out..")

    def changePassword(self, args):
        if (len(args) != 2):
            print(colored("[-] You have entered the wrong arguments!", "red"))
            print(colored("[-] Format is:\ntakeShift %date %movie %group ", "red"),
                  colored("Example: takeshift 2019-11-25 08:00 Jumanji Salesperson", "white"))#######Har ikke lavet et eksempel endnu
            return
        ret = changePassword(self.username, args[0], args[1])
        if ret == False:
            print(colored("[-] Wrong old password entered!", "red"))
            return
        print(colored("[+] Password changed!", "green"))

    def fetchListForGivenShow(self, args): #movie
        if (len(args) != 1):
            print(colored("[-] You have entered the wrong arguments!", "red"))
            print(colored("[-] Format is:\ntakeShift %date %movie %group ", "red"),
                  colored("Example: takeshift 2019-11-25 08:00 Jumanji Salesperson", "white"))#######Har ikke lavet et eksempel endnu
            return False
        shows = getShowsFromTitle(args[0])
        table = PrettyTable(["Date", "Movie Title", "Group", "User ID"])
        for show in shows:
            table.add_row(show)
        print(table)

    def listOfGroups(self):
        print(colored(listGroups(), "yellow"))

    def createGroup(self, args): #Not implemented #new group as arg
        if (len(args) != 1):
            print(colored("[-] You have entered the wrong arguments!", "red"))
            print(colored("[-] Format is:\ntakeShift %date %movie %group ", "red"),
                  colored("Example: takeshift 2019-11-25 08:00 Jumanji Salesperson", "white"))#######Har ikke lavet et eksempel endnu
            return
        if createGroup(args[0]) == False:
            print(colored("[-] Failed to add " + args[0] + " as a group","red"))
            return
        print(colored("[+]You've succesfully added " + str(args[0]) + " as a group","green"))

    def addGroup(self, args): #Name of group
        if (len(args) != 1):
            print(colored("[-] You have entered the wrong arguments!", "red"))
            print(colored("[-] Format is:\ntakeShift %date %movie %group ", "red"),
                  colored("Example: takeshift 2019-11-25 08:00 Jumanji Salesperson",
                          "white"))  #######Har ikke lavet et eksempel endnu
            return
        if addGroup(self.username, args[0]) == False:
            print(colored("[-] Failed to add you to the group " + args[0] +"!", "red"))
            return
        print(colored("[+] You've succesfully added yourself to the group " + args[0],"green"))

    def listMembersOfGroup(self,args):
        print(listMemberOfGroup(args[0]))

    def removeGroup(self, args):
        if removeUserFromGroup(self.username, args[0]) == False:
            print(colored("[-] Failed to remove you from the group " + args[0] + "!", "red"))
            return
        print(colored("[+] You've succesfully removed yourself from the group " + args[0], "green"))

    def deleteGroup(self, args):
        if deleteGroup(args[0]) == False:
            print(colored("[-] Failed to delete the group " + args[0] + "!", "red"))
            return
        print(colored("[+] You've succesfully deleted the group " + args[0], "green"))
    #today = datetime.datetime.strptime("2019-11-01 08:00", "%Y-%m-%d %H:%M")
    #date = datetime.datetime.strptime("2019-12-19 08:00", "%Y-%m-%d %H:%M")
    #x = getShowsFromDate(today, date)
    #for i in x:
    #    print(i[3])