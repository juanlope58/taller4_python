import DoubleList as dl
import SongCollection as sc
import User as u
import Song as s

class UserCollection():
    def __init__(self):
        self.__users = dl.DoubleList()
        
    def getUsers(self):
        return self.__users
    
    def add(self, u):
        self.__users.addLast(u)
        
    
    def find(self, username):
        temp = self.__users.first()
        while temp != None and temp.data.getUsername() != username :
            temp = temp.next
        
        if temp==None:
            return None
        else:
            return temp
    
    def remove(self, username):
        temp=self.find(username)
        if temp != None:
            self.__users.remove(temp)
            return  temp.data
        else:
            return None
    
    def addUserSong(self, username, songName, songList): 
        usuario=self.find(username)
        cancion=songList.find(songName)
        if usuario== None:
            print("Error: El usuario no existe")
        elif cancion==None:
            print("Error: La canción no existe")
        else:
            usuario.data.addSong(cancion.data)
            return
        
    def playUserList(self, username):
        usuario=self.find(username)
        if usuario!=None:
            usuario.data.playList()
             
        
    def print(self):
        self.__users.print()
        