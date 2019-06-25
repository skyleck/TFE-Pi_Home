import unittest

from src.be.infokea.pi_home.domain.Lamp import Lamp
from src.be.infokea.pi_home.domain.NotValidIpAddress import NotValidIpAddress
class test_Lamp(unittest.TestCase):

    def setUp(self):
        self.test = Lamp("192.255.1.1","A name", "A place", "A rigth")
    
    def test_getIp(self):
        self.assertEqual("192.255.1.1",self.test.getIp())

    def test_setIp(self):
        a = 0
        b = 0
        c = 0
        d = 0
        while a < 256: 
            ip = str(a) + "." + str(b) + "." + str(c) + "." + str(d)           
            self.test.setIp(ip)
            self.assertEqual(ip,self.test.getIp())
            d += 1
            if  d == 256:
                d = 0
                c += 1
                if c == 256:
                    c = 0
                    b += 1
                    if b == 256:
                        b = 0
                        a += 1
                        print(a)

    def test_getName(self):
        self.assertEqual("A name", self.test.getName())

    def test_setName(self):
        self.test.setName("Change name")
        self.assertEqual("Change name",self.test.getName())

    def test_getPlace(self):
        self.assertEqual("A place",self.test.getPlace())

    def test_setPlace(self):
        self.test.setPlace("Change place")
        self.assertEqual("Change place",self.test.getPlace())

    def test_getRigths(self):
        self.assertEqual("A rigth",self.test.getRigths())
    
    def test_setRigths(self):
        self.test.setRigths("Change rigth")
        self.assertEqual("Change rigth",self.test.getRigths())
