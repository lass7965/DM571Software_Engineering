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
            print(colored("You have entered the wrong arguments!", "red"))
            print(colored("Format is:\ntakeShift %date %movie %group ", "red"),colored("Example: takeshift 2019-11-25 08:00 Jumanji Salesperson", "white"))
            return False
        date = datetime.datetime.strptime(args[0]+" "+args[1], "%Y-%m-%d %H:%M")
        movie = args[2]
        group = args[3]
        for i in self.groups:
            if i[0] == group:
                ret = addShift(self.username, date, group, movie)
                if(ret == True):
                    print(colored("Successfully added shift!", "green"))
                    break
                print(colored("Failed to add shift, please try again!","red"))
                break
    def viewRoster(self, args): #Roster [Date, Movie_Title, Group, UserID]
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        shows = getShowsForUser(self.username)
        table = PrettyTable(["Date", "Movie Title", "Group", "User ID"])
        for show in shows:
            table.add_row(show)
        print(table)
    def cancelShift(self, dato, movie_title, group):
        date = datetime.datetime.strptime(dato, "%Y-%m-%d %H:%M:%S")
        temp = cancelShift(self.username, date, group, movie_title)
        if temp == True:
            print("[+] You've succesfully canceled your shift on" + str(dato))
        else:
            print("[-] You've unsuccesfully canceled your shift, please try again.")
    def listUpcommingShows(self, dato):
        today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        date = datetime.datetime.strptime(dato, "%Y-%m-%d %H:%M:%S")
        getShows(self.username, today, date, "*", "*")
        #Query to show a given number of upcomming shows
        #Maybe just output all shows, and then we can take the first X of the list to display
        print("Shows")
    def listUnoccupiedShows(self, dato):
        print("[+] Shows unoccupied for " + weeks + "in advance")
        today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        date = datetime.datetime.strptime(dato, "%Y-%m-%d %H:%M:%S")
        getShows("NULL", today, date, "*", "*")
    def logOut(self):
        print("[+] Logging out..")
    def changePassword(self, newPass):
        #Query to change current users password column and change it to newPass
        print("[+] Changing password")
        changePassword(self.username, self.password, newPass)
        self.password = newPass
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