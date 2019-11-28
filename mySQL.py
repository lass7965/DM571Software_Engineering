import mysql.connector
import datetime

try:
    logindb = mysql.connector.connect(
        host = "mysql23.unoeuro.com",
        user = "lkis_dk",
        passwd = "DM571Software",
        database="lkis_dk_db"
    )
except:
    print("Connection to the mySQL failed!")


########## Main Functions ##########
def getUserTable():
    cursor = logindb.cursor()
    cursor.execute("SELECT * FROM User")
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

########## Login Database ##########
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
    cursor = logindb.cursor()
    cursor.execute("UPDATE Login SET Password = '%s' WHERE Login.UserID = '%s' AND Login.Password = '%s'" % (newpasswd,UUID,oldpasswd))
    if(cursor.rowcount != 1):
        return False
    logindb.commit()
    cursor.close()
    return True

def updateLastLogin(username):
    UUID = getUUID(username)
    cursor = logindb.cursor()
    today = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("UPDATE Login SET Last_Login = '"+today+"' WHERE Login.UserID = '%s'" % UUID)
    logindb.commit()
    cursor.close()

########## User database ##########
def getUser(username):
    cursor = logindb.cursor()
    cursor.execute("SELECT * FROM User WHERE User.Username = '%s';" % username)
    ret = cursor.fetchone()[0]
    cursor.close()
    return ret

def updateScore(username, score):
    cursor = logindb.cursor()
    cursor.execute("UPDATE User SET Score = "+str(score)+" WHERE User.Username = '%s'" % username)
    logindb.commit()
    cursor.close()


########## Group database ##########
def getGroup(username):
    UUID = getUUID(username)
    cursor = logindb.cursor()
    cursor.execute("SELECT Groups.Grp FROM Groups WHERE Groups.UserID = '%s'" %UUID)
    ret = cursor.fetchall()
    cursor.close()
    return ret

def addGroup(username, grp):
    UUID = getUUID(username)
    cursor = logindb.cursor()
    cursor.execute("INSERT INTO Groups VALUES('%s','%s')" %(UUID,grp))
    ret = cursor.fetchmany()
    logindb.commit()
    cursor.close()
    return ret
def removeGroup(username, grp):
    UUID = getUUID(username)
    cursor = logindb.cursor()
    cursor.execute("DELETE FROM Groups WHERE Groups.UserID = '%s' AND Groups.Grp = '%s'" %(UUID,grp))
    ret = cursor.fetchmany()
    logindb.commit()
    cursor.close()
    return ret

########## Roster database ##########
def getShowsFromTitle(movie):
    cursor = logindb.cursor()
    query = "SELECT * FROM Roster WHERE Roster.Movie_Title = '%s';" %movie
    cursor.execute(query)
    ret = cursor.fetchall()
    cursor.close()
    return ret

def getShowsFromDate(fromdate):
    cursor = logindb.cursor()
    query = "SELECT * FROM Roster WHERE Roster.Date = '%s'" % fromdate
    cursor.execute(query)
    ret = cursor.fetchall()
    cursor.close()
    return ret

def getShowsFromDate(fromdate, todate):
    cursor = logindb.cursor()
    query = "SELECT * FROM Roster WHERE Roster.Date >= '%s' AND Roster.Date < '%s'" %(fromdate, todate)
    cursor.execute(query)
    ret = cursor.fetchall()
    cursor.close()
    return ret

def getShowsForUser(username):
    UUID = getUUID(username)
    cursor = logindb.cursor()
    query = "SELECT t1.Date, t1.Movie_Title, t1.Grp, Username FROM Roster AS t1 INNER JOIN User t2 ON t1.UserID = t2.UserID"
    cursor.execute(query)
    ret = cursor.fetchall()
    cursor.close()
    return ret

def getShowsForGroup(group):
    cursor = logindb.cursor()
    query = "SELECT * FROM Roster WHERE Roster.Grp = '%s'" % group
    cursor.execute(query)
    ret = cursor.fetchall()
    cursor.close()
    return ret

def addShift(username,date,grp, movie):
    UUID = getUUID(username)
    cursor = logindb.cursor()
    query = "UPDATE Roster SET UserID = '%s' WHERE Roster.Date = '%s' AND Roster.UserID IS NULL AND Roster.movie_title = '%s' AND Roster.grp = '%s' LIMIT 1" % (UUID,date,movie,grp)
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
    cursor.execute("DELETE FROM Roster WHERE Roster.UserID = '%s' AND Roster.Date = '%s' AND Roster.movie_title = '%s' AND Roster.grp = '%s' LIMIT 1" %(UUID,date,movie,grp))
    if(cursor.rowcount < 1):
        cursor.close()
        return False
    logindb.commit()
    cursor.close()
    return True
