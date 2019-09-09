import abc
import pymysql

class IData():
   
    def getDBCursor():
    	db = pymysql.connect("192.168.1.155","root","test","pi_home")
    	cursor = db.cursor()