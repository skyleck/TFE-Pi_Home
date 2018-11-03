import unittest

from src.be.infokea.pi_home.domain.User import User

class UserTest(unittest.TestCase):

    def setUp(self):
        self.user = User("Maxime","Hempte","test123")
        self.user2 = User("Maxime","Hempte","test123")
        self.user3 = User("Florent","Veys","test123")

    def test_eq(self):
        self.assertTrue(self.user == self.user2)
        self.assertFalse(self.user == self.user3)

    def test_nq(self):
        self.assertTrue(self.user != self.user3)
        self.assertFalse(self.user != self.user2)

    def test_getFirstname(self):
        self.assertEqual("Maxime", self.user.getFirstname())

    def test_setFirstname(self):
        self.user.setFirstname("Florent")
        self.assertEqual("Florent", self.user.getFirstname())

    def test_getLastname(self):
        self.assertEqual("Hempte", self.user.getLastname())

    def test_setLastname(self):
        self.user.setLastname("Veys")
        self.assertEqual("Veys", self.user.getLastname())

    def test_getPassword(self):
        self.assertEqual("test123", self.user.getPassword())

    def test_setPassword(self):
        self.user.setPassword("change123")
        self.assertEqual("change123", self.user.getPassword())
