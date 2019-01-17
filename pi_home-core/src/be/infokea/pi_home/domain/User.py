
class User(object):
    
    def __init__(self,firstname,lastname,password):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__password = password

    def __eq__(self,other):
        testFirstname = self.__firstname == other.getFirstname()
        testLastname = self.__lastname == other.getLastname()
        return testFirstname and testLastname
    
    def __ne__(self,other):
        testFirstname = self.__firstname != other.getFirstname()
        testLastname = self.__lastname != other.getLastname()
        return testFirstname or testLastname

    def getFirstname(self):
        return self.__firstname

    def setFirstname(self,firstname):
        self.__firstname = firstname

    def getLastname(self):
        return self.__lastname

    def setLastname(self,lastname):
        self.__lastname = lastname

    def getPassword(self):
        return self.__password

    def setPassword(self,password):
        self.__password = password
