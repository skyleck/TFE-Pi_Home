from src.be.infokea.pi_home.domain.Module import Module
import pymysql

class ModuleImpl():

    def __init__(self):
        self.ip = "192.168.1.155"
        self.user = "root"
        self.password = "test"
        self.database = "pi_home"
    
    def insert(self,module):
        sql = "INSERT INTO module (name,ip,state) VALUES ('"+module.getName() + "','" \
                                                + module.getIp() + "','" \
                                                + str(module.getState()) + "')"
        db = pymysql.connect(self.ip,self.user,self.password,self.database)
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
        finally:
            db.close()
    
    def select(self,id):
        sql = "SELECT * FROM module WHERE id = " + id
        db = pymysql.connect(self.ip,self.user,self.password,self.database)
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            modules = []
            for row in results:
                id = row[0]
                name = row[1]
                ip = row[2]
                state = row[3]
                modules.append(Module(id,name,ip,state))
            return modules
        finally:
            db.close()

    def selectNotNone(self):
        sql = "SELECT * FROM module where name != 'None'"
        db = pymysql.connect(self.ip,self.user,self.password,self.database)
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            modules = []
            for row in results:
                id = row[0]
                name = row[1]
                ip = row[2]
                state = row[3]
                modules.append(Module(id,name,ip,state))
            return modules
        finally:
            db.close()

    def selectAll(self):
        sql = "SELECT * FROM module"
        db = pymysql.connect(self.ip,self.user,self.password,self.database)
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            modules = []
            for row in results:
                id = row[0]
                name = row[1]
                ip = row[2]
                state = row[3]
                modules.append(Module(id,name,ip,state))
            return modules
        finally:
            db.close()
    
    def selectByName(self,name):
        sql = "SELECT * FROM module WHERE name = '" + name + "'"
        db = pymysql.connect(self.ip,self.user,self.password,self.database)
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            if(len(results) == 0):
                return None
            else:
                modules = []
                for row in results:
                    id = row[0]
                    name = row[1]
                    ip = row[2]
                    state = row[3]
                    modules.append(Module(id,name,ip,state))
                return modules
        finally:
            db.close()

    def update(self,id,module):
        sql = "UPDATE module SET name = '" + module.getName() + "'" \
                                    + " , ip = '" + module.getIp() + "'" \
                                    + " , state = '" + str(module.getState()) \
                                    + "' WHERE id = " + str(id)
        db = pymysql.connect(self.ip,self.user,self.password,self.database)
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
        finally:
            db.close()

    def delete(self,id):
        sql = "DELETE FROM module where id = " + str(id)
        db = pymysql.connect(self.ip,self.user,self.password,self.database)
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
        finally:
            db.close()