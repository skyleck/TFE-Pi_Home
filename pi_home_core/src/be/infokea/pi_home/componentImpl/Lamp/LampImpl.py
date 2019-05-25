from src.be.infokea.pi_home.domain.Lamp import Lamp

class UserLamp(object):

    def __init__(self,useDb):
        self.table = "lamps"
        self.columns = ["name","place","rigths"]
        self.columnsParams = ["id INTEGER AUTO_INCREMENT", "name varchar(100) NOT NULL","place varchar(100) NOT NULL","rigths varchar(100) NOT NULL, PRIMARY KEY(id)"]

        self.useDb = useDb

    def constructValues(self,lamp):
        return [lamp.getName(), lamp.getPlace, lamp.getRigths]

    def createTable(self):
        self.useDb.createTable(self.table,self.columnsParams)

    def dropTable(self):
        self.useDb.dropTable(self.table)

    def insert(self,element):
        self.useDb.insert(self.table, self.columns, self.constructValues(element))
    
    def select(self,columnsRef,valuesRef):
        lampsDB = self.useDb.select(self.table,columnsRef,valuesRef)
        lamps = []
        for row in lampsDB:
            name = row[1]
            place = row[2]
            rigths = row[3]
            lamp = Lamp(name,place,rigths)
            lamps.append(lamp)
        return lamps

    def selectAll(self):
        lampsDB = self.useDb.selectAll(self.table)
        lamps = []
        for row in lampsDB:
            name = row[1]
            place = row[2]
            rigths = row[3]
            lamp = Lamp(name,place,rigths)
        return lamps

    def updateName(self,oldValue,newValue,name):
        pass
