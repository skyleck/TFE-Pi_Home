from src.be.infokea.pi_home.componentImpl.IData import IData
from src.be.infokea.pi_home.domain.User import User
import pymysql

class UserImpl():

    def __init__(self, useDb):
        self.table = "user"
        self.columns = ["login","firstname", "lastname","password"]
        self.columnsParams = ["id INTEGER AUTO_INCREMENT", "login varchar(25) NOT NULL" "firstname varchar(30) NOT NULL", "lastname varchar(30) NOT NULL", "password varchar(30) NOT NULL", "PRIMARY KEY(id)"]

        self.useDb = useDb
        self.db = pymysql.connect("192.168.1.155","root","test","pi_home")
        self.cursor = self.db.cursor()
        #self.cursor = self.getDBCursor()

    def getDBCursor(self):
        db = pymysql.connect("192.168.1.155","root","test","pi_home")
        cursor = db.cursor()

    def constructValues(self,user):
        return (user.getLogin(), user.getFirstname(), user.getLastname(), user.getPassword())

    def createTable(self):
        self.useDb.createTable(self.table,self.columnsParams)

    def dropTable(self):
        self.useDb.dropTable(self.table)

    def login(self,login,password):
        sql = "SELECT * FROM user where login = '"+ login + "' AND password = '" + password + "'"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        if(len(results) == 0):
            return None;
        else:
            users = []
            for row in results:
                login = row[1]
                firstname = row[2]
                lastname = row[3]
                password = row[4]
                user = User(login, firstname, lastname, password)
                users.append(user)
            return users
    
    def insert(self,element):
        self.useDb.insert(self.table, self.columns, self.constructValues(element))

    def select(self,id):
        usersDB = self.useDb.select(self.table,id)
        users = []
        for row in usersDB:
            login = row[1]
            firstname = row[2]
            lastname = row[3]
            password = row[4]
            user = User(login, firstname, lastname, password)
            users.append(user)
        return users

    def selectAll(self):
        usersDB = self.useDb.selectAll(self.table)
        users = []
        for row in usersDB:
            login = row[1]
            firstname = row[2]
            lastname = row[3]
            password = row[4]
            user = User(login, firstname, lastname, password)
            users.append(user)
        return users
    
    def updateUser(self,id,user):
        newValues = [user.getLogin(),user.getFirstname(),user.getLastname(),user.getPassword()]
        self.useDb.update(self.table,self.columns,newValues,id)

    def updateFirstname(self,oldValue,newValue,lastname):
        self.useDb.update(self.table,"firstname",newValue,["firstname","lastname"],[oldValue,lastname])
   
    def updateLastname(self,oldValue,newValue,firstname):
        self.useDb.update(self.table,"lastname",newValue,["firstname","lastname"],[firstname,oldValue])
    
    def delete(self,id):
        self.useDb.delete(self.table,id)
        
    def close(self):
        self.useDb.close()
