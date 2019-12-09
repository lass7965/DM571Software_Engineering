import mysql.connector
import datetime

try:
    database = mysql.connector.connect(
        host = "mysql23.unoeuro.com",
        user = "lkis_dk",
        passwd = "DM571Software",
        database="lkis_dk_db"
    )
except:
    raise Exception("Connection to the mySQL failed!")


########## User table ##########
def getUserTable():
    cursor = database.cursor()
    cursor.execute("SELECT * FROM User")
    ret = cursor.fetchall()
    cursor.close()
    return ret

def getUUID(username):
    cursor = database.cursor()
    cursor.execute("SELECT User.UserID FROM User WHERE User.Username = '%s';" % username)
    try:
        ret = cursor.fetchone()[0].decode()
    except:
        return False
    cursor.close()
    return ret

def createUser(username, password, email, permission):
    cursor = database.cursor()
    try:
        today = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = "INSERT INTO User (UserID, Username, Email, Permission) VALUES(UUID(), '%s','%s',%d);" %(username, email, permission)
        cursor.execute(query)
        UUID = getUUID(username)
        query = "INSERT INTO Login VALUES('%s','%s','%s','%s');" % (UUID, password, today, today)
        cursor.execute(query)
        database.commit()
        cursor.close()
    except:
        print("User or email is already used")
        cursor.close()

########## Login table ##########
def checkPasswd(username,passwd):
    UUID = getUUID(username)
    if(UUID == False):
        return False
    cursor = database.cursor()
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
    cursor = database.cursor()
    cursor.execute("UPDATE Login SET Password = '%s' WHERE Login.UserID = '%s' AND Login.Password = '%s'" % (newpasswd,UUID,oldpasswd))
    if(cursor.rowcount != 1):
        return False
    database.commit()
    cursor.close()
    return True

def updateLastLogin(username):
    UUID = getUUID(username)
    cursor = database.cursor()
    today = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("UPDATE Login SET Last_Login = '"+today+"' WHERE Login.UserID = '%s'" % UUID)
    database.commit()
    cursor.close()

########## User database ##########
def getUser(username):
    cursor = database.cursor()
    cursor.execute("SELECT * FROM User WHERE User.Username = '%s';" % username)
    ret = cursor.fetchone()[0]
    cursor.close()
    return ret

def updateScore(username, score):
    cursor = database.cursor()
    cursor.execute("UPDATE User SET Score = "+str(score)+" WHERE User.Username = '%s'" % username)
    database.commit()
    cursor.close()


########## Group table ##########
def getGroup(username):
    UUID = getUUID(username)
    cursor = database.cursor()
    cursor.execute("SELECT Groups.Grp FROM Groups WHERE Groups.UserID = '%s'" %UUID)
    ret = cursor.fetchall()
    for i in range(len(ret)):
        ret[i] = ret[i][0]
    cursor.close()
    return ret

def listGroups():
    cursor = database.cursor()
    cursor.execute("SELECT Groups.Grp FROM Groups WHERE Groups.UserID IS NULL")
    ret = cursor.fetchall()
    cursor.close()
    for i in range(len(ret)):
        ret[i] = ret[i][0]
    return ret

def listMemberOfGroup(grp):
    cursor = database.cursor()
    try:
        cursor.execute("SELECT Username FROM (SELECT * FROM Groups WHERE Groups.grp = '%s') AS t1 INNER JOIN User t2 ON t1.UserID = t2.UserID" % grp)
        ret = cursor.fetchall()
        for i in range(len(ret)):
            ret[i] = ret[i][0]
        cursor.close()
        return ret
    except:
        return "None"

def addGroup(username, grp):
    UUID = getUUID(username)
    cursor = database.cursor()
    cursor.execute("SELECT * FROM Groups WHERE Groups.UserID IS NULL AND Groups.grp = '%s'" % grp)
    cursor.fetchmany()
    if cursor.rowcount <= 0:
        cursor.close()
        return False
    cursor.execute("INSERT INTO Groups VALUES('%s','%s')" %(UUID,grp))
    database.commit()
    cursor.close()
    return True

def createGroup(group):
    cursor = database.cursor()
    cursor.execute("INSERT INTO Groups VALUES(NULL,'%s')" %group)
    database.commit()
    cursor.close()
    return True

def removeUserFromGroup(username, grp):
    UUID = getUUID(username)
    cursor = database.cursor()
    cursor.execute("DELETE FROM Groups WHERE Groups.UserID = '%s' AND Groups.Grp = '%s'" %(UUID,grp))
    ret = cursor.fetchmany()
    database.commit()
    cursor.close()
    return ret

def deleteGroup(grp):
    cursor = database.cursor()
    cursor.execute("DELETE FROM Groups WHERE Groups.Grp = '%s'" %grp)
    if(cursor.rowcount == 0):
        cursor.close()
        return False
    database.commit()
    cursor.close()
    return True

########## Roster table ##########
def getShowsFromTitle(movie):
    cursor = database.cursor()
    query = "SELECT t1.date, t1.movie_title, t1.grp, Username FROM (SELECT * FROM Roster WHERE Roster.Movie_Title = '%s') AS t1 INNER JOIN User t2 ON t1.UserID = t2.UserID;" %movie
    cursor.execute(query)
    ret = cursor.fetchall()
    cursor.close()
    return ret

def getShowsFromDate(fromdate):
    cursor = database.cursor()
    query = "SELECT t1.date, t1.movie_title, t1.grp, Username FROM (SELECT * FROM Roster WHERE Roster.Date = '%s') AS t1 INNER JOIN User t2 ON t1.UserID = t2.UserID" % fromdate
    cursor.execute(query)
    ret = cursor.fetchall()
    cursor.close()
    return ret

def getShowsFromDate(fromdate, todate):
    cursor = database.cursor()
    query = "SELECT t1.date, t1.movie_title, t1.grp, Username FROM (SELECT * FROM Roster WHERE Roster.Date >= '%s' AND Roster.Date < '%s') AS t1 INNER JOIN User t2 ON t1.UserID = t2.UserID" %(fromdate, todate)
    cursor.execute(query)
    ret = cursor.fetchall()
    cursor.close()
    return ret

def getShowsForUser(username):
    UUID = getUUID(username)
    cursor = database.cursor()
    query = "SELECT t1.Date, t1.Movie_Title, t1.Grp, Username FROM (SELECT * FROM Roster WHERE Roster.UserID = '%s') AS t1 INNER JOIN User t2 ON t1.UserID = t2.UserID" % UUID
    cursor.execute(query)
    ret = cursor.fetchall()
    cursor.close()
    return ret

def getShowsForGroup(group):
    cursor = database.cursor()
    query = "SELECT * FROM Roster WHERE Roster.Grp = '%s'" % group
    cursor.execute(query)
    ret = cursor.fetchall()
    cursor.close()
    return ret

def addShift(username,date,grp, movie):
    UUID = getUUID(username)
    cursor = database.cursor()
    query = "UPDATE Roster SET UserID = '%s' WHERE Roster.Date = '%s' AND Roster.UserID IS NULL AND Roster.movie_title = '%s' AND Roster.grp = '%s' LIMIT 1" % (UUID,date,movie,grp)
    cursor.execute(query)
    cursor.fetchmany()
    if(cursor.rowcount<1):
        query = "INSERT INTO Roster VALUES('%s','%s','%s' ,'%s');" %(date,movie,grp,UUID)
        cursor.execute(query)
    database.commit()
    cursor.close()
    return True

def addMovie(date,grp,movie):
    cursor = database.cursor()
    cursor.execute("INSERT INTO Roster VALUES('%s','%s','%s',NULL)"%(date,movie,grp))
    database.commit()
    cursor.close()

def cancelShift(username,date,grp,movie):
    UUID = getUUID(username)
    cursor = database.cursor()
    cursor.execute("DELETE FROM Roster WHERE Roster.UserID = '%s' AND Roster.Date = '%s' AND Roster.movie_title = '%s' AND Roster.grp = '%s' LIMIT 1" %(UUID,date,movie,grp))
    if(cursor.rowcount < 1):
        cursor.close()
        return False
    database.commit()
    cursor.close()
    return True