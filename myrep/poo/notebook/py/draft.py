class Notebook:
    def __init__(self):
        self.__ligado : bool = False

    def __str__(self)  -> None:
        return self.__ligado      
    
    def status(self):
        ex = self.__ligado


