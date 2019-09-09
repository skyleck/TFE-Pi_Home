
class User(object):
    
    def __init__(self,id,login,firstname,lastname,password,authorization):
        self.__id = id
        self.__login = login
        self.__firstname = firstname
        self.__lastname = lastname
        self.__password = password
        self.__authorization = authorization

    def __eq__(self,other):
        testFirstname = self.__firstname == other.getFirstname()
        testLastname = self.__lastname == other.getLastname()
        return testFirstname and testLastname
    
    def __ne__(self,other):
        testFirstname = self.__firstname != other.getFirstname()
        testLastname = self.__lastname != other.getLastname()
        return testFirstname or testLastname

    def getId(self):
        return self.__id

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
        self.__login = login

    def getAuthorization(self):
        return self.__authorization

    def setAuthorization(self,authorization):
        self.__authorization = authorization

    def jsonFormat(self):
        return {
                'id': self.__id,
                'login': self.__login,
                'firstname': self.__firstname,
                'lastname': self.__lastname,
                'password': self.__password,
                'authorization': self.__authorization
        }
