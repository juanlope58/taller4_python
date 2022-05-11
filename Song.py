class Song():
    def __init__(self, code="", artist="", name="", album="", year=0):
        self.__code = code
        self.__name = name
        self.__artist = artist
        self.__album = album
        self.__year = year
        
    def getCode(self):
        return self.__code
    
    def getName(self):
        return self.__name
    
    def getArtist(self):
        return self.__artist
    
    def getAlbum(self):
        return self.__album
    
    def getYear(self):
        return self.__year
    
    def setCode(self, code):
        self.__code = code
    
    def setName(self, name):
        self.__name = name
        
    def setArtist(self, artist):
        self.__artist = artist
        
    def setAlbum(self, album):
        self.__album = album
        
    def setYear(self, year):
        self.__year = year
    
    def __str__(self):
        return ("Reproduciendo: "+self.__name+" - "+self.__artist)