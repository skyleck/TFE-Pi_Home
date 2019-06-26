
class Module(object):
    
    def __init__(self,id,name,ip):
        self.__id = id
        self.__name = name
        self.__ip = ip

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getIp(self):
        return self.__ip

    def setName(self,name):
        self.__name = name

    def setIp(self,ip):
        self.__ip = ip

    def jsonFormat(self):
        return {
            'id': self.__id,
            'name': self.__name,
            'ip': self.__ip
        }