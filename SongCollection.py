import DoubleList as dl
import Song as s

class SongCollection():
    def __init__(self):
        self.__songs = dl.DoubleList()
        
    def add(self, s):
        self.__songs.addLast(s)
        
    def find(self, name):
        temp = self.__songs.first()
        while temp != None and temp.data.getName() != name :
            temp=temp.next
        if temp==None:
            return None
        else:
            return temp 
    
    def remove(self, name, userList):
        cancion=self.find(name)
        temp=userList.getUsers().first()
        if cancion==None:
            print("No se eliminó la canción")
        else:
            print("Eliminada: ", end="")
            print(self.__songs.remove(cancion))
            while temp!= None:
                temp.data.removeSong(name)
                temp=temp.next
        
    def play(self):
        temp=self.__songs.first()
        while temp != None:
            print("Reproduciendo: "+ temp.data.getName() + " - " + temp.data.getArtist())
            temp=temp.next