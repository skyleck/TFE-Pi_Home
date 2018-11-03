import unittest
import pymysql
from src.be.infokea.pi_home.componentImpl.user.UserImpl import UserImpl
from src.be.infokea.pi_home.domain.User import User
from src.be.infokea.pi_home.utils.UseDB import UseDB

class test_UserImpl(unittest.TestCase):

    def setUp(self):
        self.useDBTest = UseDB("localhost","root","test","pi_home_test")
        self.userImpl = UserImpl(self.useDBTest)
        self.userImpl.dropTable()
        self.userImpl.createTable()
        self.cursor = self.useDBTest.cursor
        self.cursor.execute("INSERT INTO users(firstname,lastname,password) VALUES ('Maxime','Hempte','test123')")
        self.cursor.execute("INSERT INTO users(firstname,lastname,password) VALUES ('Florent','Veys','test123')")
        self.cursor.execute("INSERT INTO users(firstname,lastname,password) VALUES ('Bernard','Test','test123')")
        self.cursor.execute("INSERT INTO users(firstname,lastname,password) VALUES ('Adrien','Test','test123')")   
    
    def test_constructValues(self):
        user = User("Maxime","Hempte","test123")
        testValues = self.userImpl.constructValues(user)
        self.assertEqual("Maxime", testValues[0])
        self.assertEqual("Hempte", testValues[1])
        self.assertEqual("test123", testValues[2])
    
    def test_insert(self):
        user = User("Jean","Roger","test")
        self.userImpl.insert(user)
        self.cursor.execute("SELECT * FROM users")
        results = self.cursor.fetchall()
        self.assertEqual(5,len(results))
        self.assertEqual(user.getFirstname(), results[4][1])
        self.assertEqual(user.getLastname(), results[4][2])
        self.assertEqual(user.getPassword(), results[4][3])

    def test_select(self):
        user = User("Florent","Veys","test123")
        columnsRef = ["lastname"]
        valuesRef = ["Veys"]
        usersTest = self.userImpl.select(columnsRef,valuesRef)
        self.assertEqual(len(usersTest),1)
        self.assertEqual(user, usersTest[0])
        
        user1 = User("Bernard","Test","test123")
        user2 = User("Adrien","Test","test123")
        users = [user1, user2]

        columnsRef2 = ["lastname"]
        valuesRef = ["Test"]
        usersTest2 = self.userImpl.select(columnsRef2,valuesRef)
        i = 0
        nbrColumns = len(usersTest2)
        while(i < nbrColumns):
            self.assertEqual(users[i],usersTest2[i])
            i += 1
    
    def test_selectAll(self):
        user1 = User("Maxime","Hempte","test123")
        user2 = User("Florent","Veys","test123")
        user3 = User("Bernard","Test","test123")
        user4 = User("Adrien","Test","test123")

        users = [user1, user2, user3,user4]
        usersTest = self.userImpl.selectAll()
        nbrUsersTest = len(usersTest)
        i = 0
        while(i < nbrUsersTest):
            self.assertEqual(users[i], usersTest[i])
            i += 1
    

    def test_updateFirstname(self):
        user = User("Rocher","Jean","test123")
        self.userImpl.insert(user)
        user.setFirstname("Jean")
        self.userImpl.updateFirstname("Rocher","Jean","Jean")
        usersTest = self.userImpl.selectAll()
        self.assertEqual(user, usersTest[len(usersTest)-1])

    def test_updateLastname(self):
        user = User("Jean","Jean","test123")
        self.userImpl.insert(user)
        user.setLastname("Rocher")
        self.userImpl.updateLastname("Jean","Rocher","Jean")
        usersTest = self.userImpl.select(["firstname","lastname"],["Jean","Rocher"])
        self.assertEqual(user, usersTest[len(usersTest)-1])
   
    def test_delete(self):
        user1 = User("Florent","Veys","test123")
        user2 = User("Adrien","Test","test123")
        user3 = User("Bernard","Test","test123")
        
        self.userImpl.delete(["firstname"],["Florent"])
        self.cursor.execute("Select * from users")
        results = self.cursor.fetchall()
        for row in results:
            userTest = User(row[1],row[2],row[3])
            self.assertNotEqual(userTest, user1)
        self.userImpl.delete(["firstname"],["Adrien"])
        self.cursor.execute("SELECT * FROM users")
        results = self.cursor.fetchall()
        for row in results:
            userTest2 = User(row[1],row[2],row[3])
            self.assertNotEqual(userTest2,user2)
        
        userTest3 = User(results[1][1],results[1][2],results[1][3])
        self.assertEqual(user3,userTest3)

    def tearDown(self):
        self.userImpl.close()
