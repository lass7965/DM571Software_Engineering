from user import *
def loginTest(username, password):
    if checkPasswd(username,password):
        print("You are logged in!")
        userTable = getUser(username)
        currentuser = user(username, userTable[2], userTable[3], userTable[4], getGroup(username))
        #Do testing commands
        print("\n[TEST 1]\nTesting if listUsers work, expected output: True")
        test1 = listUsers() is True
        print("[TEST 1]: "+ str(test1))
        print("\n[TEST 2]\nTesting if list groups works, expected output: True")
        test2 = currentuser.listOfGroups() is True
        print("[TEST 2]: " + str(test2))
        print("\n[TEST 3]\nTesting if a group can be created, expected output: True")
        test3 = currentuser.createGroup(["testingGroup"]) is True
        print("The groups after this new group got created:\n")
        currentuser.listOfGroups()
        print("[TEST 3]: " + str(test3))
        print("\n[TEST 4]\nTesting if a group can be removed, expected output: True")
        test4 = currentuser.deleteGroup(["testingGroup"]) is True
        print("The groups after the group got removed:\n")
        currentuser.listOfGroups()
        print("[TEST 4]: " + str(test4))
        print("[TEST 5]\nTesting if list members of a group works, expected output: True")
        test5 = currentuser.listMembersOfGroup(["cleaner"]) is True
        print("[TEST 5]: " + str(test5))
        print("[TEST 6]\nTesting if user can be added to group, expected output: True")
        test6 = currentuser.addGroup(["cleaner"]) is True
        print("The group cleaner after you have added yourself:")
        currentuser.listMembersOfGroup(["cleaner"])
        print("[TEST 6]: " + str(test6))
        print("[TEST 7]\nTesting if user can be removed from a group, expected output: True")
        test7 = currentuser.removeGroup(["cleaner"]) is True
        print("The group cleaner after you have removed yourself:")
        currentuser.listMembersOfGroup(["cleaner"])
        print("[TEST 7]: " + str(test7))
        #Done testing commands
        print("Testing complete!")

def createLoginTest(username,password,email):
    createUser(username,password,email,1)
    loginTest(username,password)
loginTest("test","helloworld")