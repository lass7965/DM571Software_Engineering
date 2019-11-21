class user:
    def __init__(self, uname, passw, mail, perm, scor):
        self.username = uname
        self.password = passw
        self.email = mail
        self.permissions = perm
        self.score = scor
    def takeShift(self, date):
        print("taking shift on" + str(date))
    def viewRoster(self):
        print("Roster")
    def cancelShift(self, date):
        print("Canceling shift at" + str(date))
    def listUpcommingShows(self):
        print("Shows")
    def listUnoccupiedShows(self, weeks):
        print("Show unoccupied for " + weeks + "in advance")
    def logOut(self):
        #Maybe clean the user?
        print("Logging out..")
    def changePassword(self, newPass):
        print("Changing password")
        self.password = newPass
        #Change it in the database
    def fetchListForGivenShow(self, show):
        print("Show me da stuff")
    def listOfGroups(self):
        print("Gief me da groups")
    def createGroup(self):
        print("Creating group..")
    def addUserToGroup(self, group):
        print("Add me to this group pls")
    def listMembersOfGroup(self):
        print("Who is a member of this group?")
