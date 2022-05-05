class DoubleNode():
    def __init__(self, d=None):
        self.__data=d
        self.__next= None
        self.__prev= None
    
    @property
    def data(self):
        return self.__data
    
    @property
    def next(self):
        return self.__next
    
    @property
    def prev(self):
        return self.__prev
    
    @data.setter
    def data(self, d):
        self.__data=d
    
    @next.setter
    def next(self, n):
        self.__next=n
    
    @prev.setter
    def prev(self,n):
        self.__prev=n
    
    
    
        