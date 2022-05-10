import DoubleList as dl
import User as u

class UserCollection():
    def __init__(self):
        self.__users = dl.DoubleList()
        
    def getUsers(self):
        return self.__users
    
    # def add(self, u):
        