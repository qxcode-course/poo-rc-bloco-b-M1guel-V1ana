class Pessoa:
    def __init__(self, nome : str, age: int):
        self.__nome = nome 
        self.__age = age 

    def getAge(self):
        return self.__age
    def getName(self):
        return self.__name 
    def __str__(self):
        return f"{self.__name} : {self.__age}"
    
class Motoca:
    def __init__(self):
        self.__potencia : int = 1
        self.__time : int = 0
        self.__pessoa = None

    def __str__(self):
        return f"power:({self.__potencia}), time:({self.__time}), person:({self.__pessoa})"
        
    def inserir(self, pessoa: Pessoa) -> bool:
        if self.__pessoa is not None:
            print("fail: busy motocilce")
        
        self.__pessoa = pessoa 
        return
    
    def remover(self):
        if self.__pessoa in None:
            print("fail: empty motocycle")
            return None 
        pessoa_removida = self.__pessoa
        self.__pessoa = None
        return pessoa_removida
    
    def buyTime(self, time: int):
        self.__time += time 
    
    def drive(self, timer: int ):
        if self.__time == 0 :
            print("fail: buy time first")
        elif  self.__pessoa is None:
            print("fail: empty motocycle")
        