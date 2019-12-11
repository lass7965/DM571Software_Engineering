from user import *
def loginTest():
    print("[TEST 1]\nTesting if it is possible to create a user, expected value: True")
    test1 = createUser("test", "12345", "test@test.com", 0) is True
    print("[TEST 1]: " + str(test1))
    if checkPasswd("test","12345"):
        userTable = getUser("test")
        currentuser = user("test", userTable[2], userTable[3], userTable[4], getGroup("test"))
        #Do testing commands
        print("\n[TEST 2]\nTesting if listUsers work, expected output: True")
        test2 = listUsers() is True
        print("[TEST 2]: "+ str(test2))
        print("\n[TEST 3]\nTesting if list groups works, expected output: True")
        test3 = currentuser.listOfGroups() is True
        print("[TEST 3]: " + str(test3))
        print("\n[TEST 4]\nTesting if a group can be created, expected output: True")
        test4 = currentuser.createGroup(["testingGroup"]) is True
        print("The groups after this new group got created:\n")
        currentuser.listOfGroups()
        print("[TEST 4]: " + str(test4))
        print("\n[TEST 5]\nTesting if a group can be removed, expected output: True")
        test5 = currentuser.deleteGroup(["testingGroup"]) is True
        print("The groups after the group got removed:\n")
        currentuser.listOfGroups()
        print("[TEST 5]: " + str(test5))
        print("[TEST 6]\nTesting if list members of a group works, expected output: True")
        test6 = currentuser.listMembersOfGroup(["salesperson"]) is True
        print("[TEST 6]: " + str(test6))
        print("[TEST 7]\nTesting if user can be added to group, expected output: True")
        test7 = currentuser.addGroup(["salesperson"]) is True
        print("The group cleaner after you have added yourself:")
        currentuser.listMembersOfGroup(["salesperson"])
        print("[TEST 7]: " + str(test7))
        print("\n[TEST 8]\nTesting if shift can be enlisted, expected output: True")
        test8 = currentuser.takeShift(["2019-12-28","12:00","Jack_and_Jill" ,"salesperson"]) is True
        print("[TEST 8]: " + str(test8))
        print("\n[TEST 9]\nTesting if shift can be cancelled, expected output: True")
        test9 = currentuser.cancelShift(["2019-12-28","12:00","Jack_and_Jill" ,"salesperson"]) is True
        print("[TEST 9]: " + str(test9))
        date = datetime.datetime(2019,12,28,12,00)
        addMovie(date,"salesperson","Jack_and_Jill")
        print("[TEST 10]\nTesting if user can be removed from a group, expected output: True")
        test10 = currentuser.removeGroup(["cleaner"]) is True
        print("The group cleaner after you have removed yourself:")
        currentuser.listMembersOfGroup(["cleaner"])
        print("[TEST 10]: " + str(test10))
    cursor = database.cursor()
    cursor.execute("DELETE FROM User WHERE Username='test'")
    cursor.close()
    database.commit()
    #Done testing commands
    print("Testing complete!")
loginTest()