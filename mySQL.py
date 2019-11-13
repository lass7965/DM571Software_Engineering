import mysql.connector
import datetime
logindb = mysql.connector.connect(
    host = "mysql23.unoeuro.com",
    user = "lkis_dk",
    passwd = "DM571Software",
    database="lkis_dk_db"
)

def getFullTable():
    cursor = logindb.cursor()
    cursor.execute("SELECT * FROM Login")
    ret = cursor.fetchall()
    cursor.close()
    return ret

def getPasswd(username):
    cursor = logindb.cursor()
    cursor.execute("SELECT t1.password FROM Login AS t1 WHERE t1.username = '%s';" % username)
    ret = cursor.fetchone()[0]
    cursor.close()
    return ret

#Perhaps a more secure login, as the real password never enters the machine, and is handled by the SQL server?
def checkPasswd(username,passwd):
    try:
        cursor = logindb.cursor()
        cursor.execute("SELECT t1.username FROM Login AS t1 WHERE t1.username = '%s' AND t1.password = '%s';" % (username,passwd))
        ret = cursor.fetchone()[0]
        cursor.close()
        return True
    except:
        return False

def updateLastLogin(username):
    cursor = logindb.cursor()
    today = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("UPDATE Login SET Last_Login = '"+today+"' WHERE Login.username = '%s'" % username)
    logindb.commit()
    cursor.close()

def getLastLogin(username):
    cursor = logindb.cursor()
    cursor.execute("SELECT t1.Last_Login FROM Login AS t1 WHERE t1.username = '%s';" % username)
    return cursor.fetchone()[0]
    cursor.close()

def createUser(username, password, email, permission):
    try:
        cursor = logindb.cursor()
        today = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = "INSERT INTO Login VALUES ('%s','%s','%s',%d,'%s','%s');" %(username, password, email, permission,today,today)
        cursor.execute(query, )
        logindb.commit()
        cursor.close()
    except:
        print("User or email is already used")

def getPermissionLevel(username):
    cursor = logindb.cursor()
    cursor.execute("SELECT t1.Permission FROM Login AS t1 WHERE t1.username = '%s';" % username)
    return cursor.fetchone()[0]
    cursor.close()