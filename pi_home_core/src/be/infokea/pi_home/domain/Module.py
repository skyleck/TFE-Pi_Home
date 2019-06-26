
class Module(object):
    
    def __init__(self,id,name,ip,state):
        self.__id = id
        self.__name = name
        self.__ip = ip
        self.__state = state

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getIp(self):
        return self.__ip

    def getState(self):
        return self.__state

    def setName(self,name):
        self.__name = name

    def setIp(self,ip):
        self.__ip = ip

    def setState(self,state):
        self.__state = state

    def jsonFormat(self):
        return {
            'id': self.__id,
            'name': self.__name,
            'ip': self.__ip,
            'state':self.__state
        }