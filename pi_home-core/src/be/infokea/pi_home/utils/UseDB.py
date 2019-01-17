import pymysql

class UseDB:

    def __init__(self,ip,user,password,database):
        self.db = pymysql.connect(ip,user,password,database)
        self.cursor = self.db.cursor()

    def createTable(self, table, tabColumnsParams):
        sql = "CREATE TABLE IF NOT EXISTS " + table +  "("
        i = 0
        nbrColumns = len(tabColumnsParams)
        while(i < nbrColumns):
            if(i != 0):
                sql += ","
            sql += tabColumnsParams[i]
            i += 1
        sql = sql + ")"
        self.cursor.execute(sql)

    def dropTable(self,table):
        self.cursor.execute("DROP TABLE IF EXISTS " + table)

    def insert(self, table, tabColumns, tabValue):
        sql = "INSERT INTO " + table + "("
        i = 0
        nbrColumn = len(tabColumns)
        
        while(i < nbrColumn):
            if(i != 0):
                sql += ","
            sql += tabColumns[i]
            i += 1
        sql = sql +  ") VALUES ("
        i = 0
        nbrValue = len(tabValue)
      
        while(i < nbrColumn):
            if( i != 0):
                sql += ","
            sql = sql + "'" + tabValue[i] + "'"
            i += 1
        sql += ");"
        self.cursor.execute(sql)
        self.db.commit()

    def select(self, table,columnsRef, valuesRef):
        sql = "SELECT * FROM " + table + " where "
        nbrColumns = len(columnsRef)
        i = 0
        while(i < nbrColumns):
            if(i != 0):
                sql += " AND "
            sql = sql + columnsRef[i] + "='" + valuesRef[i] + "'"
            i += 1
        sql += ";"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results
    
    def selectAll(self,table):
        sql = "SELECT * FROM " + table
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def update(self,table,column,newValue,columnsRef,valuesRef):
        sql = "UPDATE " + table + " SET " + column + "='" + newValue + "' WHERE "
        i = 0
        nbrColumns = len(columnsRef)
        while(i < nbrColumns):
            if(i != 0):
                sql += " AND "
            sql = sql + columnsRef[i] + "='" + valuesRef[i] + "'"
            i += 1
        self.cursor.execute(sql)

    def delete(self,table,columnsRef,valuesRef):
        sql = "DELETE FROM " + table + " WHERE "
        i = 0
        nbrColumns = len(columnsRef)
        while(i < nbrColumns):
            if(i != 0):
                sql += " AND "
            sql = sql + columnsRef[i] + "='" + valuesRef[i] + "'"
            i += 1
        print(sql)
        self.cursor.execute(sql)
        self.db.commit()

    def close(self):
        self.db.close()
