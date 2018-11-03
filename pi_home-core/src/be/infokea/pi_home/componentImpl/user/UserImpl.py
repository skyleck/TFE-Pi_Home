from src.be.infokea.pi_home.componentImpl.IData import IData
from src.be.infokea.pi_home.domain.User import User
class UserImpl(IData):

    def __init__(self, useDb):
        self.table = "users"
        self.columns = ["firstname", "lastname","password"]
        self.columnsParams = ["id INTEGER AUTO_INCREMENT", "firstname varchar(30) NOT NULL", "lastname varchar(30) NOT NULL", "password varchar(30) NOT NULL", "PRIMARY KEY(id)"]

        self.useDb = useDb

    def constructValues(self,user):
        return (user.getFirstname(), user.getLastname(), user.getPassword())

    def createTable(self):
        self.useDb.createTable(self.table,self.columnsParams)

    def dropTable(self):
        self.useDb.dropTable(self.table)

    def insert(self,element):
        self.useDb.insert(self.table, self.columns, self.constructValues(element))

    def select(self,columnsRef,valuesRef):
        usersDB = self.useDb.select(self.table,columnsRef,valuesRef)
        users = []
        for row in usersDB:
            firstname = row[1]
            lastname = row[2]
            password = row[3]
            user = User(firstname, lastname, password)
            users.append(user)
        return users

    def selectAll(self):
        usersDB = self.useDb.selectAll(self.table)
        users = []
        for row in usersDB:
            firstname = row[1]
            lastname = row[2]
            password = row[3]
            user = User(firstname,lastname,password)
            users.append(user)
        return users
    
    def updateFirstname(self,oldValue,newValue,lastname):
        self.useDb.update(self.table,"firstname",newValue,["firstname","lastname"],[oldValue,lastname])
   
    def updateLastname(self,oldValue,newValue,firstname):
        self.useDb.update(self.table,"lastname",newValue,["firstname","lastname"],[firstname,oldValue])
    
    def delete(self,columnsRef,valuesRef):
        self.useDb.delete(self.table,columnsRef,valuesRef)
        
    def close(self):
        self.useDb.close()
