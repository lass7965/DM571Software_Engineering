class user:
    def __init__(self, uname, passw, mail, perm, scor):
        self.username = uname
        self.password = passw
        self.email = mail
        self.permissions = perm
        self.score = scor
    def takeShift(self, date):
        #Query for creating a shift
        #Maybe a query to check if the given date and time is occupied?
        #Make a query request with the data inside of the userClass
        print("taking shift on" + str(date))
    def viewRoster(self): #Roster [Date, Movie_Title, Group, UserID]
        #Query to output the whole roster as a list
        print("Roster")
    def cancelShift(self, date):
        #Query to remove a shift from the DB given a date
        print("Canceling shift at" + str(date))
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
