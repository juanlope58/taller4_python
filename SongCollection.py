import DoubleList as dl
import Song as s

class SongCollection():
    def __init__(self):
        self.__songs = dl.DoubleList()
        
    def add(self, s):
        self.__songs.addLast(s)
        
    # def find(name):
    #     return DoubleNode
    
    # def remove(self, name, userList):
        
    def play(self):
        self.__songs.print()