from user import *
def loginTest(username, password):
    if checkPasswd(username,password):
        print("You are logged in!")
        userTable = getUser(username)
        currentuser = user(username, userTable[2], userTable[3], userTable[4], getGroup(username))
        #Do testing commands
        print("\n[TEST 1]\nTesting if listUsers work, expected output: Type(PrettyTable)")
        test1 = type(listUsers()) is PrettyTable
        print("[TEST 1]: "+ str(test1))
        print("\n[TEST 2]\nTesting if list groups works, expected output: Type(List)")
        test2 = type(currentuser.listOfGroups()) is list
        print("[TEST 2]: " + str(test2))
        print("\n[TEST 3]\nTesting if a group can be created, expected output: Type(Boolean)")
        test3 = type(currentuser.createGroup(["testingGroup"])) is bool
        print("The groups after this new group got created:\n")
        currentuser.listOfGroups()
        print("[TEST 3]: " + str(test3))
        print("\n[TEST 4]\nTesting if a group can be removed, expected output: Type(Boolean)")
        test4 = type(currentuser.deleteGroup(["testingGroup"])) is bool
        print("The groups after the group got removed:\n")
        currentuser.listOfGroups()
        print("[TEST 4]: " + str(test4))
        print("[TEST 5]\nTesting if list members of a group works, expected output: Type(Boolean)")
        test5 = type(currentuser.listMembersOfGroup(["cleaner"])) is bool
        print("[TEST 5]: " + str(test5))
        print("[TEST 6]\nTesting if user can be added to group, expected output: Type(Boolean)")
        test6 = type(currentuser.addGroup(["cleaner"])) is bool
        print("The group cleaner after you have added yourself:")
        currentuser.listMembersOfGroup(["cleaner"])
        print("[TEST 6]: " + str(test6))
        print("[TEST 7]\nTesting if user can be removed from a group, expected output: Type(Boolean)")
        test7 = type(currentuser.removeGroup(["cleaner"])) is bool
        print("The group cleaner after you have removed yourself:")
        currentuser.listMembersOfGroup(["cleaner"])
        print("[TEST 7]: " + str(test7))
        #Done testing commands
        print("Testing complete!")

def createLoginTest(username,password,email):
    createUser(username,password,email,1)
    loginTest(username,password)
loginTest("test","helloworld")