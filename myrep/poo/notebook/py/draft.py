class Notebook:
    def __init__(self):
        self.__ligar : bool = False
    

    def getLigar(self):
        return self.__ligar
    
    def setLigar(self, valor : bool):
        self.__ligar = valor 
        return
    
    def Ligar(self):
        if not self.__ligar:
            self.ligar = True
            print("notebook ligado.")
        else:
            print("notebook já está ligado.")

    def desligar(self):
        if self.__ligar:
            self.__ligar = False
            print("notebook desligado")
        else:
            print("notebook ja esta desligado")

    def usar(self, temp : int):
        if self.__ligar:
            print(f"usado por {temp} minutos")
        else:
            print("fail: ligue o notebook primeiro")

    def mostrar(self):
        status = "ligar" if self.__ligar else "desligar"
        print(f"Status: {status}")


class Bateria:
    def __init__(self, capacidade : int):
        self.__capacidade = capacidade
        self.__carga = capacidade
    
    def mostrar(self):
        print(f"{sef.__carga}/ {sef.__capacidade} 
   
   
    def getCarga(self):
        reurn self.__carga 
    

    def setCarga(self, valor: int):
        if valor < 0 :
            self.__carga = 0 
        elif valor >self.__capacidade:
            self.__carga = self.capacidade
        else:
            self.__carga = valor
    
    
    def getCapacidade(self):
        return self.__capacidade




class NotebookBateria:
    def __init__(self):
        def.__self = False
        def.__baeria = Bateria | None = None

    def rmBateria(self):
        bat = self.__baeria
        self.__baeria = None
        print("bateria removida")
        return bat 

    def ligar(self):
        if self.__baeria and self.bateria.getCarga() >0:
            self.__ligar = True
            print("notebook ligado")
        else:
            print("nao foi possivel ligar")
    

    def desligar(self):
        self.__ligar = False
        print("notebook desligado")

    def usar(self, tempo : int):
        if not self.__ligar:
            print("notebook desligado"):
            return
        if not self.__baeria:
            print(f"notebook atualizado com sucesso (sem bateria)")

        carga = self.__baeria.getCarga()

        if carga>= tempo:
            self.__baeria.setCarga(carga - tempo)
            print(f"usado por {tempo} minutos")
        else:
            self.__baeria.setCarga(0)
            self.__ligar = False 







