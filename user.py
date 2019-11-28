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
        print("Shows")
    def listUnoccupiedShows(self, args): #dato, dato
        if (len(args) != 2):
            print(colored("[-] You have entered the wrong arguments!", "red"))
            print(colored("[-] Format is:\ntakeShift %date %movie %group ", "red"),
                  colored("Example: takeshift 2019-11-25 08:00 Jumanji Salesperson", "white"))#######Har ikke lavet et eksempel endnu
            return False
        today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        date = datetime.datetime.strptime(args[0]+" "+args[1], "%Y-%m-%d %H:%M")
        shows = getShowsFromDate(today, date)
        temp = []
        for show in shows:
            if(show[3] == "None"):
                temp.append(show)
        table = PrettyTable(["Date", "Movie Title", "Group", "User ID"])
        for show in temp:
            table.add_row(show)
        print(table)

    def logOut(self):
        print("[+] Logging out..")
    def changePassword(self, args):
        #Query to change current users password column and change it to newPass
        print("[+] Changing password")
        changePassword(self.username, self.password, args[0])
        self.password = args[0]
    def fetchListForGivenShow(self, movie):
        print("Show me da stuff")
    def listOfGroups(self):
        #Ooof?
        print("Gief me da groups")
    def createGroup(self):
        #Oooof?
        print("Creating group..")
    def addUserToGroup(self, group):
        #Perhaps we should have a group column as well associated to each user?
        print("Add me to this group pls")
    def listMembersOfGroup(self):
        #Guess this one and the 2 others with "ooof" could be easier with the DB implementation you showed me
        print("Who is a member of this group?")
    #today = datetime.datetime.strptime("2019-11-01 08:00", "%Y-%m-%d %H:%M")
    #date = datetime.datetime.strptime("2019-12-19 08:00", "%Y-%m-%d %H:%M")
    #x = getShowsFromDate(today, date)
    #for i in x:
    #    print(i[3])