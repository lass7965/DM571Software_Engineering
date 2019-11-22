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
        print("Roster")
    def cancelShift(self, dato, movie_title, group):
        date = datetime.datetime.strptime(dato, "%Y-%m-%d %H:%M:%S")
        temp = cancelShift(self.username, date, group, movie_title)
        if temp == True:
            print("[+] You've succesfully canceled your shift on" + str(dato))
        else:
            print("[-] You've unsuccesfully canceled your shift, please try again.")
    def listUpcommingShows(self, number):
        #Query to show a given number of upcomming shows
        #Maybe just output all shows, and then we can take the first X of the list to display
        print("Shows")
    def listUnoccupiedShows(self, weeks):
        #This one will be difficult?
        print("Show unoccupied for " + weeks + "in advance")
    def logOut(self):
        #Maybe clean the user?
        print("Logging out..")
    def changePassword(self, newPass):
        #Query to change current users password column and change it to newPass
        print("Changing password")
        self.password = newPass
    def fetchListForGivenShow(self, show):
        #Maybe just iterate through the whole roster, looking for shows equal to "show"
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
