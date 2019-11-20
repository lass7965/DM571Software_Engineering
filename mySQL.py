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

def getFullTable():
    cursor = logindb.cursor()
    cursor.execute("SELECT * FROM Login")
    ret = cursor.fetchall()
    cursor.close()
    return ret

def getUUID(username):
    cursor = logindb.cursor()
    cursor.execute("SELECT User.UserID FROM User WHERE User.Username = '%s';" % username)
    ret = cursor.fetchone()[0].decode()
    cursor.close()
    return ret

def getPasswd(username):
    UUID = getUUID(username)
    cursor = logindb.cursor()
    cursor.execute("SELECT t1.password FROM Login AS t1 WHERE t1.UserID = '%s';" % UUID)
    ret = cursor.fetchone()[0]
    cursor.close()
    return ret

#Perhaps a more secure login, as the real password never enters the machine, and is handled by the SQL server?
def checkPasswd(username,passwd):
    UUID = getUUID(username)
    cursor = logindb.cursor()
    cursor.execute("SELECT t1.UserID FROM Login AS t1 WHERE t1.UserID = '%s' AND t1.Password = '%s';" % (UUID, passwd))
    try:
        cursor.fetchone()[0] #This command fails if user and password does not match.
        cursor.close()
        return True
    except:
        cursor.close()
        return False

def updateLastLogin(username):
    UUID = getUUID(username)
    cursor = logindb.cursor()
    today = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("UPDATE Login SET Last_Login = '"+today+"' WHERE Login.UserID = '%s'" % UUID)
    logindb.commit()
    cursor.close()

def getLastLogin(username):
    UUID = getUUID(username)
    cursor = logindb.cursor()
    cursor.execute("SELECT t1.Last_Login FROM Login AS t1 WHERE t1.UserID = '%s';" % UUID)
    ret = cursor.fetchone()[0]
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

def getPermissionLevel(username):
    UUID = getUUID(username)
    cursor = logindb.cursor()
    cursor.execute("SELECT t1.Permission FROM Login AS t1 WHERE t1.UserID = '%s';" % UUID)
    ret = cursor.fetchone()[0]
    cursor.close()
    return ret