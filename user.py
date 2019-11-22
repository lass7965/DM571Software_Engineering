import datetime
from mySQL import *
class user:
    def __init__(self, uname, passw, mail, perm, scor, uniqueID, groups):
        self.username = uname
        self.password = passw
        self.email = mail
        self.permissions = perm
        self.score = scor
        self.groups = groups
    def takeShift(self, dato, movie_title, group):
        date = datetime.datetime.strptime(dato, "%Y-%m-%d %H:%M:%S")
        for i in self.groups:
            if i == group:
                print("[+] Taking shift on" + str(dato))
                addShift(self.username, date, group, movie_title)
                break
        print("[-] You've entered a wrong command. ")
    def viewRoster(self): #Roster [Date, Movie_Title, Group, UserID]
        #Query to output the whole roster as a list
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        getShows(self.username, date, "*", "*", "*")
        print("Roster")
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

        getShows()
        username, fromdate, todate, grp, movie
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
