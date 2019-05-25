
class User(object):
    
    def __init__(self,login,firstname,lastname,password):
        self.__login = login
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

    def getLogin(self):
        return self.__login

    def setLogin(self,login):
        return self.__login

    def jsonFormat(self):
        return {
                'login': self.__login,
                'firstname': self.__firstname,
                'lastname': self.__lastname,
                'password': self.__password
        }
