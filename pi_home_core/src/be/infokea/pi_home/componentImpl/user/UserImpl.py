from src.be.infokea.pi_home.componentImpl.IData import IData
from src.be.infokea.pi_home.domain.User import User
import pymysql
import hashlib

class UserImpl():

    def __init__(self):
        self.ip = "192.168.50.1"
        self.user = "root"
        self.password = "test"
        self.database = "pi_home"

    def getDBCursor(self):
        db = pymysql.connect("192.168.50.1","root","test","pi_home")
        cursor = db.cursor()

    def login(self,login,password):
        sql = "SELECT * FROM user where login = '"+ login + "' AND password = sha2('" + password + "salt',512)"
        db = pymysql.connect(self.ip,self.user,self.password,self.database)
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            if(len(results) == 0):
                return None
            else:
                users = []
                for row in results:
                    id = row[0]
                    login = row[1]
                    firstname = row[2]
                    lastname = row[3]
                    password = row[4]
                    authorization = row[5]
                    user = User(id, login, firstname, lastname, password,authorization)
                    users.append(user)
                return users
        finally:
            db.close()

    def getUserByLogin(self,login):
        sql = "SELECT * FROM user where login = '" + login + "'"
        db = pymysql.connect(self.ip,self.user,self.password,self.database)
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            if(len(results) == 0):
                return None
            else:
                users = []
                for row in results:
                    id = row[0]
                    login = row[1]
                    firstname = row[2]
                    lastname = row[3]
                    password = row[4]
                    authorization = row[5]
                    user = User(id, login, firstname, lastname, password,authorization)
                    users.append(user)
                return users
        finally:
            db.close()

    def insert(self,user):
        sql = "INSERT INTO user (login,firstname,lastname,password,authorization) VALUES ('"+ user.getLogin() + "','"  \
                                                                    + user.getFirstname() + "','" \
                                                                    + user.getLastname() + "'," \
                                                                    + "sha2('" + user.getPassword() + "salt',512)," \
                                                                    + str(user.getAuthorization()) + ")"
        db = pymysql.connect(self.ip,self.user,self.password,self.database)
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
        finally:
            db.close()

    def select(self,id):
        sql = "SELECT * FROM user WHERE id = " + id
        db = pymysql.connect(self.ip,self.user,self.password,self.database)
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            users = []
            for row in results:
                id = row[0]
                login = row[1]
                firstname = row[2]
                lastname = row[3]
                password = row[4]
                authorization = row[5]
                user = User(id,login, firstname, lastname, password,authorization)
                users.append(user)
            return users
        finally:
            db.close()

    def selectAll(self):
        sql = "SELECT * FROM user"
        db = pymysql.connect(self.ip,self.user,self.password,self.database)
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            users = []
            for row in results:
                id = row[0]
                login = row[1]
                firstname = row[2]
                lastname = row[3]
                password = row[4]
                authorization = row[5]
                user = User(id,login, firstname, lastname, password,authorization)
                users.append(user)
            return users
        finally:
            db.close()
    
    def updateUser(self,id,user):
        sql = "UPDATE user SET login ='" + user.getLogin() + "'" \
                            + " , firstname ='" + user.getFirstname() + "'" \
                            + " , lastname = '" + user.getLastname() + "'" \
                            + " , password = " + "sha2('" + user.getPassword() + "salt',512)" \
                            + " , authorization = " + str(user.getAuthorization()) \
                            + " WHERE id = " + str(id)

        db = pymysql.connect(self.ip,self.user,self.password,self.database)
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
        finally:
            db.close()
    
    def delete(self,id):
        sql = "DELETE FROM user where id = " + str(id)
        db = pymysql.connect(self.ip,self.user,self.password,self.database)
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
        finally:
            db.close()
        
