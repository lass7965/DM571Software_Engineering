import mysql.connector
import datetime
import bytestring
try:
    logindb = mysql.connector.connect(
        host = "mysql23.unoeuro.com",
        user = "lkis_dk",
        passwd = "DM571Software",
        database="lkis_dk_db"
    )
except:
    print("Connection to the mySQL failed!")

def getUserTable():
    cursor = logindb.cursor()
    cursor.execute("SELECT * FROM User")
    ret = cursor.fetchall()
    cursor.close()
    return ret

def getRosterTable():
    cursor = logindb.cursor()
    cursor.execute("SELECT * FROM Roster")
    ret = cursor.fetchall()
    cursor.close()
    return ret

def getUUID(username):
    cursor = logindb.cursor()
    cursor.execute("SELECT User.UserID FROM User WHERE User.Username = '%s';" % username)
    try:
        ret = cursor.fetchone()[0].decode()
    except:
        return False
    cursor.close()
    return ret

#Perhaps a more secure login, as the real password never enters the machine, and is handled by the SQL server?
def checkPasswd(username,passwd):
    UUID = getUUID(username)
    if(UUID == False):
        return False
    cursor = logindb.cursor()
    cursor.execute("SELECT t1.UserID FROM Login AS t1 WHERE t1.UserID = '%s' AND t1.Password = '%s';" % (UUID, passwd))
    try:
        cursor.fetchone()[0] #This command fails if user and password does not match.
        cursor.close()
        return True
    except:
        cursor.close()
        return False

def changePassword(username, oldpasswd, newpasswd):
    UUID = getUUID(username)
    if(UUID == False):
        return False

def updateLastLogin(username):
    UUID = getUUID(username)
    cursor = logindb.cursor()
    today = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("UPDATE Login SET Last_Login = '"+today+"' WHERE Login.UserID = '%s'" % UUID)
    logindb.commit()
    cursor.close()

def createUser(username, password, email, permission):
    cursor = logindb.cursor()
    try:
        today = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = "INSERT INTO User (UserID, Username, Email, Permission) VALUES(UUID(), '%s','%s',%d);" %(username, email, permission)
        cursor.execute(query)
        UUID = getUUID(username)
        query = "INSERT INTO Login VALUES('%s','%s','%s','%s');" % (UUID, password, today, today)
        cursor.execute(query)
        logindb.commit()
        cursor.close()
    except:
        print("User or email is already used")
        cursor.close()

def updateScore(username, score):
    cursor = logindb.cursor()
    cursor.execute("UPDATE User SET Score = "+str(score)+" WHERE User.Username = '%s'" % username)
    logindb.commit()
    cursor.close()

def updateGroup(username, group):
    cursor = logindb.cursor()
    cursor.execute("UPDATE User SET Groups = "+group+" WHERE User.Username = '%s'" % username)
    logindb.commit()
    cursor.close()

def getUser(username):
    cursor = logindb.cursor()
    cursor.execute("SELECT * FROM User WHERE User.Username = '%s';" % username)
    ret = cursor.fethone()[0]
    cursor.close()
    return ret

def addShift(username,date,grp, movie):
    UUID = getUUID(username)
    cursor = logindb.cursor()
    query = "UPDATE Roster SET UserID = '%s' WHERE Roster.Date = '%s' AND Roster.UserID IS NULL AND Roster.movie_title = '%s' AND Roster.grp = '%s'" % (UUID,date,movie,grp)
    cursor.execute(query)
    cursor.fetchmany()
    if(cursor.rowcount<1):
        query = "INSERT INTO Roster VALUES('%s','%s','%s' ,'%s');" %(date,movie,grp,UUID)
        cursor.execute(query)
    logindb.commit()
    cursor.close()
    return True

def addMovie(date,grp,movie):
    cursor = logindb.cursor()
    cursor.execute("INSERT INTO Roster VALUES('%s','%s','%s',NULL)"%(date,movie,grp))
    logindb.commit()
    cursor.close()

def cancelShift(username,date,grp,movie):
    UUID = getUUID(username)
    cursor = logindb.cursor()
    cursor.execute("DELETE FROM Roster WHERE Roster.UserID = '%s' AND Roster.Date = '%s' AND Roster.movie_title = '%s' AND Roster.grp = '%s'" %(UUID,date,movie,grp))
    logindb.commit()
    cursor.close()

def showShifts(username, date, deltadate, grp, movie):


date = datetime.datetime(2019,11,21,21,0)
cancelShift("Lasse",date,"None","Movie#1")