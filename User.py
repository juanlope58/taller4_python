import DoubleList as dl
import Song as s

class User():
    def __init__(self, username):
        self.__username = username
        self.__userSongList = dl.DoubleList()
        
    def getUsername(self):
        return self.__username
    
    def setUsername(self, u):
        self.__username = u
        
    def addSong(self, s):
        self.__userSongList.addFirst(s)
        
    def findSong(self, name):
        temp=self.__userSongList.first()
        while temp != None and temp.data.getName() != name:
            temp =temp.next
        if temp==None:
            return None
        else:
            return temp
         
    def removeSong(self, name):
        temp=self.findSong(name)
        while temp!= None:
            self.__userSongList.remove(temp)
            temp=temp.next
        
    def playList(self):
        temp=self.__userSongList.first()
        while temp!=None:
            print(self.__username + " está reproduciendo: "+temp.data.getName())
            temp=temp.next
    
    def __str__(self):
        return self.__username
        
    
        