import re
from src.be.infokea.pi_home.domain.NotValidIpAddress import NotValidIpAddress

class Lamp(object):

    def __init__(self,ip,name,place,rigths):
        self.setIp(ip)
        self.__name = name
        self.__place = place
        self.__rigths = rigths

    def getIp(self):
        return self.__ip

    def setIp(self,ip):
        check = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",ip)
        if check == False :
            raise NotValidIpAddress("This is not a valid ip address")
        a,b,c,d = ip.split(".")
        if int(a) > 255 or int(b) > 255 or int(c) > 255 or int(d) > 255 :
            raise NotValidIpAddress(ip + ":This is not a valid ip address")
        self.__ip = ip
        
    def getName(self):
        return self.__name

    def setName(self,name):
        self.__name = name

    def getPlace(self):
        return self.__place

    def setPlace(self,place):
        self.__place = place

    def getRigths(self):
        return self.__rigths

    def setRigths(self,rigths):
        self.__rigths = rigths
