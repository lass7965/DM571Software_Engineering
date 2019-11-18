class user:
    def __init__(self, uname, passw, mail, perm):
        self.username = uname
        self.password = passw
        self.email = mail
        self.permissions = perm
    def takeShift(self, date):
        print("taking shift on" + str(date))
    def viewRoser(self):
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